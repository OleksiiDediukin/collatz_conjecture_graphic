import tkinter as tk
from tkinter import ttk


class PanelFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.draw_button = ttk.Button(self, text="Start",
                                      command=lambda: master.start_draw(*self.get_range()))
        self.start_entry = tk.Entry(self, width=20, bd=3)
        self.finish_entry = tk.Entry(self, width=20, bd=3)
        self.start_entry.grid(row=1, column=1)
        self.finish_entry.grid(row=1, column=2)
        self.draw_button.grid(row=2, column=1)

    def get_range(self):
        start = int(self.start_entry.get())
        finish = int(self.finish_entry.get())
        return start, finish
