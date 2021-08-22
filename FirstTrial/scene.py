from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        
        square = Square()
        square.rotate(PI/4)

        self.play(Create(square))
        self.play(Transform(square,circle))
        self.play(FadeOut(square))

class MovingFrame(Scene):
    def construct(self):
        text = MathTex(
                "A^2","+","B^2","=","C^2")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[0],buff=.1)
        framebox2 = SurroundingRectangle(text[2],buff=.1)
        framebox3 = SurroundingRectangle(text[4],buff=.1)
        self.embed() 
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait()
        self.play(ReplacementTransform(framebox2,framebox3))
        self.wait()

class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2,-1,0])
        dot2 = Dot([2,1,0])
        line = Line(dot.get_center(),dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal Distance")
        b2 = Brace(line,direction=line.copy().rotate(PI/2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")

        self.wait()
        self.play(Write(dot))
        self.play(Write(dot2))
        self.play(Write(line))
        self.play(Write(b2))
        self.play(Write(b2text))
        self.play(Write(b1))
        self.play(Write(b1text))
        self.wait(duration=3)
        
        # self.add(line,dot,dot2,b1,b1text,b2,b2text)

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1,color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot,dot2))
        self.play(MoveAlongPath(dot,circle),run_time=2)
        self.wait()