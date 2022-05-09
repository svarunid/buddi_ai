from model import QuadraticModel

x, y = [], []

with open("./data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line[: len(line) - 1]
        a, b = map(float, line.split("\t"))
        x.append(a)
        y.append(b)

model = QuadraticModel(x, y, QuadraticModel.MEAN_ABSOLUTE_ERROR)
# params ending are excluded values
model.grid_search((-5, 6), (-5, 6), (-5, 6))

if __name__ == "__main__":
    print("MEAN_ABSOLUTE_ERROR")
    print("ERROR: ", model.error)
    print("PARAMS: ", model.params)
    print()

model = QuadraticModel(x, y, QuadraticModel.MEAN_SQUARED_ERROR)
model.grid_search((-5, 6), (-5, 6), (-5, 6))

if __name__ == "__main__":
    print("MEAN_SQUARED_ERROR")
    print("ERROR: ", model.error)
    print("PARAMS: ", model.params)
    print()

    print("PREDICT for x=-50: ", model.predict(-50))
    print("PREDICT for x=50: ", model.predict(50))