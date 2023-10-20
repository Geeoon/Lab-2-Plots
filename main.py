from matplotlib import pyplot as plt
import numpy as np


if __name__ == '__main__':
    x_points = [70, 80, 90, 100, 110, 120]
    y_points = [14.54, 13.86, 12.03, 11.5, 10.95, 9.92]
    y_error = [0.264, 0.372, 0.0263, 0.258, 0.114, 0.135]
    
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    ax.errorbar(x_points, y_points, y_error, fmt='o', linewidth=2, capsize=6)
    ax.set(xlim=(0, 150), xticks=np.arange(0, 150, 5),
           ylim=(0, 20), yticks=np.arange(0, 20))
    plt.show()