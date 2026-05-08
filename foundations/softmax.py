import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        if z is None:
            return z
        softmax: NDArray[np.float64]
        maxVal: np.float64 = np.max(z)
        print(maxVal)

        # Find the sum for the denominator portion of softmax, then apply
        denominator = 0
        for j in range(len(z)):
            denominator += np.exp(z[j] - maxVal)
        print(denominator)
        for i in range(len(z)):
            numerator = np.exp(z[i] - maxVal)
            z[i] = np.round((numerator / denominator), 4)
        return z