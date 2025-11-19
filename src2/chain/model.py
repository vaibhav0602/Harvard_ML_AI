#https://github.com/jmschrei/torchegranate/blob/main/tutorials/B_Model_Tutorial_5_Markov_Chains.ipynb
import numpy
import torch
from torchegranate.distributions import Categorical
from torchegranate.distributions import ConditionalCategorical
from torchegranate.markov_chain import MarkovChain
# Define starting probabilities
start = Categorical([[
    0.5,                   #sun
    0.5]]                   #rain
)

# Define transition model
transitions = ConditionalCategorical([
 [   [0.8,                           #sun to sun
    0.2],                           #sun to rain,
    [ 0.3,                          #"rain", "sun",
    0.7]                            #"rain", "rain",
]])

# Create Markov chain
model = MarkovChain([start, transitions])

# Sample 50 states from chain
print(model.sample(4))
