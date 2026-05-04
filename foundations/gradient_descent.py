class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0 :
            return round(init, 5)
        elif init == 0:
            return float(init)
        else:
            grad_val: int = init
            for i in range(iterations):
                grad_val = grad_val - (learning_rate * (2 * grad_val))
            return round(grad_val, 5)