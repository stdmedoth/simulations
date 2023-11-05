import numpy as np
import matplotlib.pyplot as plt


class Matrix :
    def __init__(self, dim):
        self.data = np.zeros(dim)