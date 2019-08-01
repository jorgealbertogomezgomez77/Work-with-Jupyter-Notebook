
import numpy
import matplotlib.pyplot as plt

num_points = 100
num_simulations = 300
PI_list = []


def one_simulation():
    mean = 0
    coord_X = numpy.random.uniform(0, 1, num_points).tolist()
    coord_Y = numpy.random.uniform(0, 1, num_points).tolist()

    for i in range(num_points):
        dentro = 0
        circulo = (coord_X[i] * coord_X[i] + coord_Y[i] * coord_Y[i])
        if (circulo < 1):
            dentro += 1

    float_value = float(dentro)
    float_PI = (float_value * 4) / num_points
    PI_list.append(float_PI)
    mean += float_PI

for k in range(num_simulations):
    one_simulation()
    PI = mean / num_simulations

print(PI)
plt.plot(PI_list)
plt.show()