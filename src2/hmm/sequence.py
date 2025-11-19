from model import model
import numpy

# Observed data
observations = [
    "umbrella",
    "umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella"
]
X = numpy.array([[[['umbrella', 'no umbrella'].index(char)] for char in observations]])
print(X.shape)

# Predict underlying states
predictions = model.predict(X)
#for prediction in predictions:
#    print(model.states[prediction].name)

print("sequence: {}".format(''.join(observations)))
print("hmm pred: {}".format(''.join([str(y.item()) for y in predictions[0]])))


#110111100