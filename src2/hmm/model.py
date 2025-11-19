#https://github.com/jmschrei/torchegranate/blob/main/tutorials/B_Model_Tutorial_4_Hidden_Markov_Models.ipynb
from pomegranate import *
from torchegranate.distributions import Categorical
from pomegranate.distributions import ConditionalCategorical
import numpy
from torchegranate.hmm import DenseHMM

# Observation model for each state
sun = Categorical([[
    0.2,                             #"umbrella"
     0.8                             #"no umbrella"
]])

rain = Categorical([[     0.9,       #"umbrella"
                        0.1          #No umbrella
]])
model = DenseHMM([sun,rain],starts=[.5,.5],edges=[[0.8, 0.2],[0.3, 0.7]])

#this is another way to initialize and proceed with the model if all the details are not provided initially
'''
model=DenseHMM()
model.add_distributions([sun, rain])
model.add_edge(model.start, sun, 0.5)
model.add_edge(model.start, rain, 0.5)
model.add_edge(sun, sun, 0.8)
model.add_edge(sun, rain, 0.2)
model.add_edge(rain, rain, 0.7)
model.add_edge(rain, sun, 0.3)'''


# Transition model
'''transitions = numpy.array(
   [ [[0.8, 0.2], # Tomorrow's predictions if today = sun
     [0.3, 0.7]] # Tomorrow's predictions if today = rain
])
'''