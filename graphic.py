import matplotlib.pyplot as plt


def DrawGraphic(x_min, x_max, y_min, y_max, x, y, description):
    plt.ylabel('Название вертикальной оси'),
    plt.xlabel('Название горизонтальной оси')
    plt.title(description)
    plt.plot(x, y, 'r-')
    plt.axis([x_min, x_max, y_min, y_max])
    plt.grid()
    plt.show()
