import numpy as np
import matplotlib.pyplot as plt


def r_cubic_spline(x_data, y_data):
    r = 2 + np.sqrt(3)
    a = y_data
    n = len(a) - 1
    h = x_data[1] - x_data[0]
    b = np.zeros(n)
    c = np.zeros(n + 1)
    d = np.zeros(n)
    e = np.zeros(n + 1)
    alpha = np.zeros(n + 1)

    def setup_e():
        for i in range(n + 1):
            if i == 0:
                e[i] = ((3 * r) / (2 * h)) * ((a[1] - a[0]) / h)
            elif i == n:
                e[i] = 0
            else:
                e[i] = (3 / np.pow(h, 2)) * (a[i - 1] - (2 * a[i]) + a[i + 1])

    def setup_alpha():
        for i in range(n + 1):
            if i == 0:
                alpha[i] = e[i] / r
            elif i == n:
                alpha[i] = e[i]
            else:
                alpha[i] = (e[i] - alpha[i - 1]) / r

    def setup_c():
        for i in range(n, -1, -1):
            if i == n:
                c[i] = alpha[i]
            else:
                c[i] = alpha[i] - c[i + 1] / r

    def setup_b_and_d():
        for i in range(n):
            b[i] = (a[i + 1] - a[i]) / h - (2 * c[i] + c[i + 1]) / 3 * h
            d[i] = 1 / (3 * h) * (c[i + 1] - c[i])

    setup_e()
    setup_alpha()
    setup_c()
    setup_b_and_d()

    x_array = []
    y_array = []

    for i in range(n):
        interval_x = np.linspace(x_data[i], x_data[i+1], 100)
        interval_y = ((a[i] +
                      b[i] * (interval_x - x_data[i])) +
                      c[i] * np.pow(interval_x - x_data[i], 2) +
                      d[i] * np.pow(interval_x - x_data[i], 3))

        x_array += interval_x.tolist()
        y_array += interval_y.tolist()

    plt.figure(figsize=(8, 6))
    plt.plot(x_data, y_data, 'o', label='Data Points')
    plt.plot(x_array, y_array, '-', label='r-Cubic Spline')
    plt.title('r-Cubic Spline Interpolation')
    plt.xlabel('---------- X AXIS ----------')
    plt.ylabel('---------- Y AXIS ----------')
    plt.legend()
    plt.grid(True)
    plt.show()


x = 6, 13, 20, 27
y = 75, 78, 72, 68

r_cubic_spline(x, y)

