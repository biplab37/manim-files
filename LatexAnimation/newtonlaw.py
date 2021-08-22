from manim import *

class NewtonLaw(Scene):
	def construct(self):
		title = Text("Newton's Law of motion")
		title2 = Text("Newton's Law").to_corner(UP)

		square = Square(color=GREEN,fill_opacity=1)

		arrow = Arrow(start=RIGHT,end=3*RIGHT,buff=0)

		arrow_text = Text("F").move_to(2*RIGHT+0.5*UP)
		mass_text = Text("m")

		picture = VGroup(square,arrow_text,arrow,mass_text)
		picture2 = picture.copy().move_to(2*DOWN).scale(0.9)

		equation1 = Tex("{{F}}orce = {{m}}ass $\\times$ {{a}}cceleration")
		equation2 = Tex("{{F}} = {{m}}$\\times${{a}}")

		self.play(Write(title))
		self.play(ReplacementTransform(title,title2))
		self.play(DrawBorderThenFill(square))
		self.play(Indicate(mass_text))
		self.play(Create(arrow),Write(arrow_text))
		self.play(Indicate(arrow_text))
		self.play(Transform(picture,picture2))
		self.play(Write(equation1))
		self.play(TransformMatchingTex(equation1,equation2))
		self.wait(duration=3)
		self.play(Indicate(equation2),FadeOut(picture))
		self.wait(3)

class MovingObject(Scene):
	def construct(self):
		# Surface
		surface = Line(4*LEFT,4*RIGHT).move_to(DOWN)

		# Object
		square = Square(color=BLUE,fill_opacity=1).move_to(-2*RIGHT)

		# Force
		force = Arrow(start=-RIGHT,end=RIGHT,buff=0,color=RED)

		obj = VGroup(square,force)

		# Trajectory

		trajectory = Line(-RIGHT,3*RIGHT)

		self.play(Create(surface))
		self.play(DrawBorderThenFill(square))

		self.play(Create(force))

		self.play(MoveAlongPath(obj,trajectory))
		self.wait(2)


class Masses(Scene):
	def construct(self):

		obj = VGroup()

		for i in range(4):
			surface = Line(8*LEFT,8*RIGHT).move_to(DOWN)
			square = Square(color=BLUE,fill_opacity=1).move_to(-6*RIGHT)
			force = Arrow(start=-5*RIGHT,end=-RIGHT,buff=0,color=RED)

			obj += VGroup(surface,square,force).scale(0.5)

		obj.arrange(DOWN).shift(2*LEFT)
		self.add(obj)
