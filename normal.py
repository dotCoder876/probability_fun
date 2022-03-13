
import matplotlib.pyplot as plt
import numpy as np
# Import math Library
import math 
class Normal:
    def __init__(self, mean=0, variance=1) -> None:
        self.mean = mean
        self.variance = variance
    def pdf(self):
        plt.style.use('_mpl-gallery')
        # make data
        sd = math.sqrt(self.variance)
        x = np.linspace(self.mean - 3 *sd, self.mean + 3 * sd, 100)
        normalize = lambda x: (x - self.mean) / sd
        square_then_halve_negative = lambda z: (z ** 2) * (-0.5)

        y = (1/(sd * math.sqrt(2 * math.pi))) * np.exp(square_then_halve_negative(normalize(x)))
        # plot
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
        ax.set(xlim=(self.mean - 3 *sd, self.mean + 3 * sd), xticks=np.linspace(self.mean - 3 *sd, self.mean + 3 * sd, 10),
            ylim=(0, 1.1/(sd * math.sqrt(2 * math.pi))), yticks=np.linspace(0, (1/(sd * math.sqrt(2 * math.pi))), 10))
        plt.show()
Normal().pdf()