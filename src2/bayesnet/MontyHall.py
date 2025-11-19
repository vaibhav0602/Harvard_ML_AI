import numpy
import torch
from torchegranate.distributions import Categorical
from torchegranate.distributions import ConditionalCategorical
guest = Categorical([[1./3, 1./3, 1./3]])
prize = Categorical([[1./3, 1./3, 1./3]])



probs = numpy.array([[
     [[0.0, 0.5, 0.5], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
     [[0.0, 0.0, 1.0], [0.5, 0.0, 0.5], [1.0, 0.0, 0.0]],
     [[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.5, 0.5, 0.0]]
]])

monty = ConditionalCategorical(probs)
from torchegranate.bayesian_network import BayesianNetwork

model = BayesianNetwork([guest, prize, monty], [(guest, monty), (prize, monty)])
X = torch.tensor([[0, 1, -1],
                  [0, 2, -1],
                  [2, 1, -1]])

X_masked = torch.masked.MaskedTensor(X, mask=X >= 0)


model.predict(X_masked)