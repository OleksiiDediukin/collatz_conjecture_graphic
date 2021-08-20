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
        self.figure.add_subplot(1, 1, 1)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def drawing(self, start, finish):
        for num in range(start, finish):
            sequence = calculations.generate_sequence(num)
            x = [0]
            y = [num]
            while True:
                try:
                    self.update_graph(x, y, sequence)
                    time.sleep(0.2)
                except StopIteration:
                    break

    @staticmethod
    def update_graph(x, y, sequence):
        x.append(len(x))
        y.append(next(sequence))
        plt.clf()
        plt.plot(x, y)
        plt.draw()
        plt.gcf().canvas.flush_events()

