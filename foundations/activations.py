import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        sigmoid_calc: np.float64
        for i in range(len(z)):
            sigmoid_calc = np.float64(1 / (1 + np.exp(-1 * z[i])))
            z[i] = np.round(sigmoid_calc, 5)
        return z

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        for i in range(len(z)):
            relu_calc = np.float64(np.max([0, z[i]]))
            z[i] = np.round(relu_calc, 5)
        return z
