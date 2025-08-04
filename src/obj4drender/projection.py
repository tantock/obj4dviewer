import math
import numpy as np


class Projection:
    def __init__(self, render):
        NEAR = render.camera.near_plane
        FAR = render.camera.far_plane
        RIGHT = math.tan(render.camera.h_fov / 2)
        LEFT = -RIGHT
        TOP = math.tan(render.camera.v_fov / 2)
        BOTTOM = -TOP
        THERE = math.tan(render.camera.d_fov / 2)
        HERE = -THERE

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = 2 / (THERE - HERE)
        m33 = (FAR + NEAR) / (FAR - NEAR)
        m43 = -2 * NEAR * FAR / (FAR - NEAR)
        self.projection_matrix = np.array([
            [m00, 0, 0, 0, 0],
            [0, m11, 0, 0, 0],
            [0, 0, m22, 0, 1],
            [0, 0, 0, m33, 1],
            [0, 0, 0, m43, 0]
        ])

        HW, HH, HD = render.H_WIDTH, render.H_HEIGHT, render.H_DEPTH
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0, 0],
            [0, -HH, 0, 0, 0],
            [0, 0, HD, 0, 0],
            [0, 0, 0, 1, 0],
            [HW, HH, HD, 0, 1]
        ])