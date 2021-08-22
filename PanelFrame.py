import tkinter as tk
from tkinter import ttk


class PanelFrame(tk.Frame):
    def __init__(self, master, width=300, height=600, *args, **kwargs):
        super().__init__(master)
        self.master = master
        self.canvas = None
        self.width = width
        self.height = height
        self.draw_button = None
        self.start_entry = None
        self.finish_entry = None
        self.rendering()

    def rendering(self):
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.grid()
        self.draw_button = ttk.Button(self, text="Start",
                                      command=lambda: self.master.start_draw(*self.get_range()))
        self.start_entry = tk.Entry(self, width=20, bd=3)
        self.finish_entry = tk.Entry(self, width=20, bd=3)
        tk.Label(self, text="From: ", font=("Arial", 10)).place(x=10, y=20)
        self.start_entry.place(x=55, y=20)
        tk.Label(self, text="To: ", font=("Arial", 10)).place(x=10, y=60)
        self.finish_entry.place(x=55, y=60)
        self.draw_button.place(x=12, y=100)

    def get_range(self):
        start = int(self.start_entry.get())
        finish = int(self.finish_entry.get())
        return start, finish
