from manim import *

class InteractiveDevelopment(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(BLUE)
		square = Square()

		self.play(Write(square))

		self.wait()

		self.embed()