import matplotlib.pyplot as plt
import numpy as np
# Import math Library
import math 
class Binomial:
    def __init__(self, number, probability):
        self.number = number
        self.probability = probability
    def pmf(self):
        plt.style.use('_mpl-gallery')

        # make data:
        x = np.arrange(0, self.number, 1, dtype=int)
        print(math.floor(self.number * self.probability))
        print(math.ceil(self.number * self.probability))
        y = np.fromfunction(lambda k: (self.probability**k) * ((1-self.probability)**(self.number - k)), (self.number + 1, ), like=x)
        y = np.fromfunction(lambda k: math.comb(int(self.number),k) * (self.probability**k) * ((1-self.probability)**(self.number - k)), (self.number + 1, ), like=x)
        print(x)
        print(y)
        # plot
        fig, ax = plt.subplots()

        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))

        plt.show()
Binomial(10, 0.2).pmf()