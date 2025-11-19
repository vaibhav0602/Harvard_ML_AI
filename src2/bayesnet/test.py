#https://github.com/jmschrei/torchegranate/blob/main/examples/Bayesian_Network_Monty_Hall.ipynb
import numpy
import torch
from torchegranate.distributions import Categorical
from torchegranate.distributions import ConditionalCategorical
from torchegranate.bayesian_network import BayesianNetwork

# Define the mappings used throughout the network:
# Rain:       0 = "none",  1 = "light",  2 = "heavy"
# Maintenance: 0 = "yes",   1 = "no"
# Train:      0 = "on time", 1 = "delayed"
# Appointment: 0 = "attend",  1 = "miss"

# Rain node has no parents
rain = Categorical([[0.7, 0.2, 0.1]])


# Track maintenance node is conditional on rain (Parent Shape: 3, Child Shape: 2)
# Using a 3x2 probability tensor
maintenance_probs = numpy.array([[
    [0.4, 0.6],  # When rain is 0 ("none"): yes, no
    [0.2, 0.8],  # When rain is 1 ("light"): yes, no
    [0.1, 0.9]   # When rain is 2 ("heavy"): yes, no
]])
maintenance = ConditionalCategorical(probs=maintenance_probs)


# Train node is conditional on rain and maintenance (Parent Shapes: 3, 2; Child Shape: 2)
# Using a 3x2x2 probability tensor
train_probs = numpy.array([
    # Rain Index 0 ("none")
    [[
        [0.8, 0.2],  # Maint 0 ("yes"): on time, delayed
        [0.9, 0.1]   # Maint 1 ("no"): on time, delayed
    ],
    # Rain Index 1 ("light")
    [
        [0.6, 0.4],  # Maint 0 ("yes"): on time, delayed
        [0.7, 0.3]   # Maint 1 ("no"): on time, delayed
    ],
    # Rain Index 2 ("heavy")
    [
        [0.4, 0.6],  # Maint 0 ("yes"): on time, delayed
        [0.5, 0.5]   # Maint 1 ("no"): on time, delayed
    ]]
])

train = ConditionalCategorical(probs=train_probs)


# Appointment node is conditional on train (Parent Shape: 2, Child Shape: 2)
# Using a 2x2 probability tensor
appointment_probs = numpy.array([[
    [0.9, 0.1],  # When train is 0 ("on time"): attend, miss
    [0.6, 0.4]   # When train is 1 ("delayed"): attend, miss
]])
appointment = ConditionalCategorical(probs=appointment_probs)


# Create a Bayesian Network
model = BayesianNetwork([rain, maintenance, train, appointment], [(rain, maintenance), (rain, train),(maintenance, train),(train,appointment)])

print("Bayesian Network successfully created and baked using Pomegranate 1.0+ syntax.")

X=torch.tensor([[0,0,-1,0]])
X_masked=torch.masked.MaskedTensor(X, mask=X >= 0)
print(model.predict(X_masked))

################################discarded###########################################
'''
# In v1.0+, you use add_distributions to add the distributions as nodes
# The order added here determines their index in the model's internal list
model.add_distributions(distributions={rain, maintenance, train, appointment})

# Add edges connecting nodes
# The order of parent edges added to a child matters for ConditionalCategorical tensors
model.add_edge(rain, maintenance)
# Edge order for 'train' matters: rain corresponds to the first dimension (3), maintenance the second (2)
model.add_edge(rain, train)
model.add_edge(maintenance, train)
model.add_edge(train, appointment)

# Finalize model structure and compile underlying data structures
model.bake()



x = torch.tensor([[2, 0, 0, 0]])
mask = torch.tensor([[True, True, False, True]])
x_masked = torch.masked.MaskedTensor(x, mask=mask)
logp = model.log_probability(x_masked)

#logp = model.log_probability(x, mask='mask')
#p = torch.exp(logp)
print(f"Log P(Appointment=attend | Rain=heavy, Maint=yes): {logp.item():.4f}")
print(f"P(Appointment=attend | Rain=heavy, Maint=yes): {p.item():.4f}")

train_probs = numpy.array([
    # Maint 0 ("none")
    [[
        [0.8, 0.2],  # Rain 0 ("yes"): on time, delayed
        [0.6, 0.4],  # Rain 1 ("yes"): on time, delayed
        [0.4, 0.6],  # Rain 2 ("yes"): on time, delayed
    ],
    # Maint 1 ("light")
    [
        [0.9, 0.1],   # Rain 0 ("no"): on time, delayed
        [0.7, 0.3],   # Rain 1 ("no"): on time, delayed
        [0.5, 0.5]  # Rain 2 ("no"): on time, delayed
    ]]

])


'''

