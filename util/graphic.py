import matplotlib.pyplot as plt
from util.RedConsts import condition


def draw_graphic(x_min, x_max, y_min, y_max, x,y, description):
    # plt.ylabel('Y')
    # plt.xlabel('X')
    plt.title(description)
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'r-')
    plt.axis([x_min, x_max, y_min, y_max])
    plt.grid()
    plt.show()
