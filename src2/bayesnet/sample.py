import pomegranate

from collections import Counter

from test import model
from torchegranate.distributions import ConditionalCategorical
def generate_sample():

    # Mapping of random variable name to sample generated
    sample = {}

    # Mapping of distribution to sample generated
    parents = {}

    # Loop over all states, assuming topological order
    for state in model.distributions:

        # If we have a non-root node, sample conditional on parents
        if isinstance(state, ConditionalCategorical):
            sample[state.name] = state.sample(parent_values=parents)

        # Otherwise, just sample from the distribution alone
        else:
            sample[state.name] = state.sample()

        # Keep track of the sampled value in the parents mapping
        parents[state] = sample[state.name]

    # Return generated sample
    return sample

# Rejection sampling
# Compute distribution of Appointment given that train is delayed
N = 10000
data = []
for i in range(N):
    sample = generate_sample()
    if sample["train"] == "delayed":
        data.append(sample["appointment"])
print(Counter(data))

