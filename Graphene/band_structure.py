from manim import *
import numpy as np

class BandStructure(ThreeDScene):
    def ff(self, kx, ky, a=1.0):
        return np.exp(1j * a * kx / np.sqrt(3)) + 2 * np.exp(-1j * a * kx / (2*np.sqrt(3))) * np.cos(a * ky / 2)
    def energy(self, kx, ky):
        return np.abs(self.ff(kx, ky))
    def construct(self):
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(u, v, self.energy(u, v)),
            u_range=[-2*PI, 2*PI],
            v_range=[-2*PI, 2*PI],
        )
        surface2 = Surface(
            lambda u, v: axes.c2p(u, v, -self.energy(u, v)),
            u_range=[-2*PI, 2*PI],
            v_range=[-2*PI, 2*PI],
        )
        # self.interactive_embed()
        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
        self.wait(1)
        self.play(Create(surface), Create(surface2))
        self.wait(5)
