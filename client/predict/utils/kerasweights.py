import numpy as np


class KerasWeightsHelper():
    """ FEDn helper class for keras.Sequential. """

    def save_model(self, weights, path=None):
        if not path:
            path = self.get_tmp_path()

        weights_dict = {}
        for i,w in enumerate(weights):
            weights_dict[str(i)] = w
        np.savez_compressed(path, **weights_dict)
        return path

    def load_model(self, path="weights.npz"):

        a = np.load(path)
        weights = []
        for i in range(len(a.files)):
            weights.append(a[str(i)])
        return weights
