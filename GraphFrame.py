import time
import matplotlib
import calculations
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")


class GraphFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master)
        self.figure = plt.figure(figsize=(10, 10), dpi=100)
        plt.ion()

        plt.gca().set_ylim([0, 1000])
        plt.gca().set_xlim([0, 100])
        self.figure.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.max_x = 0
        self.max_y = 0

    def drawing(self, start, finish):
        for num in range(start, finish):
            sequence = calculations.generate_sequence(num)
            x = [0]
            y = [num]
            while True:
                try:
                    self.update_graph(x, y, sequence)
                    time.sleep(0.002)
                except StopIteration:
                    break

    def update_graph(self, x, y, sequence):
        x.append(len(x))
        y.append(next(sequence))
        plt.clf()
        plt.plot(x, y)
        self.update_max_cords(x[-1], y[-1])
        plt.gca().set_xlim([0, max(100, self.max_x+20)])
        plt.gca().set_ylim([0, max(1000, self.max_y+100)])
        plt.draw()
        plt.gcf().canvas.flush_events()

    def update_max_cords(self, x, y):
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

