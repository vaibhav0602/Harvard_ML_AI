import torch
from test import model

# Observation: [Rain, Maintenance, Train, Appointment]
x = torch.tensor([[0, 1, 0, 0]])  # shape: (n_samples, n_features)

# Compute log-probability
logp = model.log_probability(x)

# Convert to normal probability
p = torch.exp(logp)

print(f"Log Probability: {logp.item()}")
print(f"Probability: {p.item()}")