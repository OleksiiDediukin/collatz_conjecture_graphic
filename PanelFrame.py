import tkinter as tk
from tkinter import ttk


class PanelFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.draw_button = ttk.Button(self, text="Start")
        self.start_entry = tk.Entry(self, width=20, bd=3)
        self.finish_entry = tk.Entry(self, width=20, bd=3)
        self.start_entry.grid(row=1, column=1)
        self.finish_entry.grid(row=1, column=2)
        self.draw_button.grid(row=2, column=1, sticky=tk.N+tk.S+tk.W+tk.E)