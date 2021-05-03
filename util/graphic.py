import matplotlib.pyplot as plt


def DrawGraphic(x_min, x_max, y_min, y_max, x, y, description):
    plt.ylabel('Y'),
    plt.xlabel('X')
    plt.title(description)
    plt.plot(x, y, 'r-')
    plt.axis([x_min, x_max, y_min, y_max])
    plt.grid()
    plt.show()
