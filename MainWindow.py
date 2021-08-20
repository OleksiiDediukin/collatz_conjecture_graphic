import tkinter as tk
from GraphFrame import GraphFrame
from PanelFrame import PanelFrame


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        tk.Tk.geometry(self, "1300x600")
        tk.Tk.wm_title(self, "Collatz")

        self.graph_frame = GraphFrame(self, wigth=900, height=600)
        self.panel_frame = PanelFrame(self)
        self.graph_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.panel_frame.pack(side=tk.LEFT, padx=10, pady=10)

    def start_draw(self, start, finish):
        """Calls the drawing methods on the graph frame."""
        self.graph_frame.drawing(start, finish)



