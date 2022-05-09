from model import LinearModel
import numpy as np

x, y = [], []

with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line[: len(line) - 1]
        a, b = map(float, line.split("\t"))
        x.append(a)
        y.append(b)

x = np.array(x)
y = np.array(y)
x2 = np.array([i ** 2 for i in x])

model = LinearModel(x2, x, y)
model.find_beta()

if __name__ == "__main__":
    print()
    print(model.beta_matrix)
