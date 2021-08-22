from manim import *

class TexTransformation(Scene):
	def construct(self):
		tex1 = MathTex(r"\frac{1}{ {{G_E}} } - \frac{\Lambda}{\pi}")
		tex2 = MathTex(r"{{G_E}}")

		# self.add(tex1,tex2)
		self.play(Create(tex1,run_time=2))

		self.wait(duration=6)
		self.play(TransformMatchingTex(tex1,tex2,run_time=3))

class Anagram(Scene):
	def construct(self):
		title = Text("Anagram",color=BLUE).to_corner(UP)
		src = Text("the morse code")
		des = Text("here come dots")
		self.add(title)
		self.play(Write(src))
		self.wait()
		self.play(TransformMatchingShapes(src,des,path_arc=-PI/2))

		self.wait(2)

