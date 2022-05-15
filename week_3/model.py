import numpy as np


class LinearModel:
    def __init__(self, x2, x,  y):
        self.X = np.array([x2, x, np.ones(61)])
        self.y = y

    def find_beta(self):
        X = self.X
        Y = self.y

        beta_m_1 = np.linalg.inv(np.dot(X, X.T))
        beta_m_2 = np.dot(X, Y)

        self.beta_matrix = np.dot(beta_m_1, beta_m_2)

    def predict(self, x):
        return self.beta_matrix[0] * (x ** 2) + self.beta_matrix[1] * x + self.beta_matrix[2]
