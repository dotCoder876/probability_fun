
import matplotlib.pyplot as plt
import numpy as np
# Import math Library
import math 
class UniformRectangular:
    def __init__(self, left_endpoint, right_endpoint) -> None:
        self.left_endpoint = left_endpoint
        self.right_endpoint = right_endpoint
    def pdf(self):
        plt.style.use('_mpl-gallery')
        # make data
        x = np.linspace(self.left_endpoint,  self.right_endpoint, 100)
        y = np.full_like(x,1/(self.right_endpoint - self.left_endpoint))
        # plot
        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth=2.0)
        ax.set(xlim=(self.left_endpoint * 0.9, self.right_endpoint * 1.1), xticks=np.linspace(self.left_endpoint * 0.9, self.right_endpoint * 1.1, 10),
            ylim=(0, 1.1/(self.right_endpoint - self.left_endpoint)), yticks=np.linspace(0, 1.1/(self.right_endpoint - self.left_endpoint), 10))
        plt.show()
UniformRectangular(1, 10).pdf()