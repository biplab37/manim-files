from manim import *
import numpy as np

class FunctionPlotSin(Scene):
	def construct(self):
		axes = Axes(
			x_range = [-10,10,1],
			y_range = [-1.5,1.5,1],
			axis_config = {"color":GREEN},
			tips=False)

		sin_plot = axes.get_graph(lambda x: np.sin(x) , color=BLUE)
		self.add(axes,sin_plot)