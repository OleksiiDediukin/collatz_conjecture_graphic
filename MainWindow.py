import tkinter as tk
import ttk
from GraphFrame import GraphFrame
from PanelFrame import PanelFrame


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        tk.Tk.wm_title(self, "Collatz")
        self.width = 1200
        self.height = 600
        self.graph_frame = GraphFrame(self, width=self.width*0.7, height=self.height)
        self.panel_frame = PanelFrame(self, width=self.width*0.3, height=self.height)
        self.graph_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.panel_frame.pack(side=tk.LEFT, padx=10, pady=10)

    def start_draw(self, start, finish):
        """Calls the drawing methods on the graph frame."""
        self.graph_frame.drawing(start, finish)



