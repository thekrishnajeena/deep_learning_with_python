# class to chain those layers, wraps a list of layers and exposes a __call__() method that calles the underlying layers on the inputs in order
# also features a weights property to easily keep track of the layers' parameters

class NaiveSequential:
    def __init__(self, layers):
        self.layers = layers

    def __call__(self, inputs):
        x = inputs
        for layer in self.layers:
            x = layer(x)
        return x
    
    @property
    def weights(self):
        weights = []
        for layer in self.layers:
            weights += layer.weights
        return weights