import numpy as np
from numpy.typing import NDArray

class Solution:

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is (n, m), weights is (m,) -> return (n,) predictions
        # Round to 5 decimal places
        pass

        n: int = len(X)
        m: int = len(X[0])
        dot_prod: NDArray[np.float64] = []
        print(X, weights)
        print(f"n:{n}, m:{m}")

        for i in range(n):
            dot_prod_pos: np.float64 = 0.0
            for j in range(m):
                cur_pos = X[i, j] * weights[j]
                dot_prod_pos += cur_pos
            dot_prod.append(dot_prod_pos)
        return np.round(dot_prod, 5)
        # return np.round(np.matmul(X, weights), 5)



    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute mean squared error between predictions and ground truth
        # Round to 5 decimal places
        pass

        n: int = len(model_prediction)
        m: int = len(model_prediction[0])
        MSE: np.float64 = 0.0

        for i in range(n):
            for j in range(m):
                MSE += (model_prediction[i, j] - ground_truth[i,j])**2
                print(MSE)
        MSE /= n # where n is the elements of each column in the vector
        return np.round(MSE, 5)

