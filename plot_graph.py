import matplotlib.pyplot as plt

class Graph:

    def __init__(self):
        self.fig_ = plt.figure()
        self.ax_ = self.fig_.add_subplot(111)
        self.ax_.grid()
        self.save_name = "output/sample.jpg"

    def draw(self, x, y, color, label):
        self.ax_.plot(x, y, color=color, label=label)
        self.ax_.legend()

    def save(self):
        self.fig_.savefig(self.save_name)
