import numpy as np
from numpy.typing import NDArray


class Solution:

    def binary_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: true labels (0 or 1)
        # y_pred: predicted probabilities
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        # pass
        if len(y_true) != len(y_pred):
            print("y_true and y_pred lengths don't match!")
            return 0
        
        loss: np.float64 = 0.0000
        small_e: np.float64 = 1e-7
        n: int = len(y_pred)

        for i in range(n):
            adjust_y_pred = y_pred[i] + small_e
            loss += (y_true[i] * np.log(adjust_y_pred)) + ((1 - y_true[i]) * np.log(1 - adjust_y_pred))
            # print(loss)
        loss *= -(1/n)    
        return np.round(loss, 4)
        
    def categorical_cross_entropy(self, y_true: NDArray[np.float64], y_pred: NDArray[np.float64]) -> float:
        # y_true: one-hot encoded true labels (shape: n_samples x n_classes)
        # y_pred: predicted probabilities (shape: n_samples x n_classes)
        # Hint: add a small epsilon (1e-7) to y_pred to avoid log(0)
        # return round(your_answer, 4)
        # pass

        loss: np.float64 = 0.0000
        small_e: np.float64 = 1e-7
        n_samples: int = len(y_true[0])
        n_classes: int = len(y_true)

        for c in range(n_classes):
            for i in range(n_samples):
                # print(f"({c}, {i})", y_true[c, i], y_pred[c, i])
                adjust_y_pred = y_pred[c, i] + small_e
                loss += (y_true[c, i] * np.log(adjust_y_pred))
        loss *= -(1/n_classes)
        return np.round(loss, 4)



