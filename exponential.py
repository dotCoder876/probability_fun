
import matplotlib.pyplot as plt
import numpy as np
# Import math Library
import math 
class Exponential:
    def __init__(self, rate) -> None:
        self.rate = rate
    def pdf(self):
        plt.style.use('_mpl-gallery')
        # make data
        x_max = abs(math.log(0.01*self.rate))/3
        x = np.linspace(0,x_max, 100)
        y = self.rate * np.exp(-1 * self.rate * x)
        # plot
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
        ax.set(xlim=(0, 5.0 / self.rate), xticks=np.linspace(0, 5.0 / self.rate, 10),
            ylim=(0, 1.2 * self.rate), yticks=np.linspace(0, 1.2 * self.rate, 10))
        plt.show()
Exponential(50).pdf()