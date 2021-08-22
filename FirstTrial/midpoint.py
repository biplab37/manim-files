from manim import *
import numpy as np

class MidPoint(Scene):
	"""
	Show the method of calculating midpoint of a line segment
	"""
	def construct(self):

		text1 = Text("Calculating mid point of a segment")
		transformed_text = Text("Midpoint").to_corner(UP)
		dot1 = Dot([-2,0,0])
		dot2 = Dot([2,0,0])
		line = Line(dot1,dot2)

		circle1 = Circle(radius=2.5).move_to(dot1.get_center())
		circle2 = Circle(radius=2.5).move_to(dot2.get_center())

		intersection1 = Dot([0,np.sqrt(2.25),0],color=YELLOW)
		intersection2 = Dot([0,-np.sqrt(2.25),0],color=YELLOW)

		line2 = Line(intersection1,intersection2,color=ORANGE)

		midpoint = Dot([0,0,0],color=RED)

		text2 = Text("midpoint").scale(0.5).shift(UP)
		arrow = Arrow(start=text2.get_center(),end=midpoint.get_center())

		self.play(Write(text1))

		self.wait()

		self.play(ReplacementTransform(text1,transformed_text))

		self.play(Write(dot1))
		self.play(Write(dot2))

		self.play(Write(line))

		self.wait(duration=2)

		self.play(Write(circle1),duration=2)
		self.play(Write(circle2),duration=2)

		self.play(Write(intersection1),Write(intersection2))

		self.play(FadeOut(circle1),FadeOut(circle2))

		self.play(Write(line2))

		self.play(Write(midpoint))
		self.play(FadeOut(line2),FadeOut(intersection2),FadeOut(intersection1))
		self.play(ReplacementTransform(transformed_text,text2),Write(arrow))

		self.wait(duration=3)

		# self.add(dot1,dot2,line,circle1,circle2,intersection1,intersection2,line2,midpoint)