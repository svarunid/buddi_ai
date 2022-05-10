from typing import List, Tuple

class QuadraticModel:
    MEAN_ABSOLUTE_ERROR = 0
    MEAN_SQUARED_ERROR = 1

    def __init__(self, x: List[int], y: List[int], error_metric: int):
        self.x = x
        self.y = y
        self.error_metric = error_metric

    def _calc_mean_absolute_error(self, y: List[int], predicted_y: List[int]):
        error_sum = 0
        for i in range(len(y)):
            error_sum += abs(y[i] - predicted_y[i])
        return error_sum / len(y)

    def _calc_mean_squared_error(self, y: List[int], predicted_y: List[int]):
        error_sum = 0
        for i in range(len(y)):
            error_sum += (y[i] - predicted_y[i]) ** 2
        return error_sum / len(y)

    def _calc_error(self, a: int, b: int, c: int):
        predicted_y = []
        for x in self.x:
            predicted_y.append(a * (x ** 2) + b * x + c)

        error = None
        if self.error_metric == self.MEAN_ABSOLUTE_ERROR:
            error = self._calc_mean_absolute_error(self.y, predicted_y)
        else:
            error = self._calc_mean_squared_error(self.y, predicted_y)
        return error

    def grid_search(self, a: Tuple[int], b: Tuple[int], c: Tuple[int]):
        min_error = float("inf")
        for i in range(a[0], a[1]):
            for j in range(b[0], b[1]):
                for k in range(c[0], c[1]):
                    error = self._calc_error(i, j, k)
                    if error < min_error:
                        self.params = (i, j, k)
                        min_error = error

        self.error = min_error
        return self

    def predict(self, x: int):
        return self.params[0] * (x ** 2) + self.params[1] * x + self.params[2]
