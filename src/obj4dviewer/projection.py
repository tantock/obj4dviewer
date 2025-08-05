import math
import numpy as np
from obj4dviewer.camera_view_setting import CameraViewSetting

class Perspective:
    def __init__(self, view_settings:CameraViewSetting):
        NEAR = view_settings.near_plane
        FAR = view_settings.far_plane
        RIGHT = math.tan(view_settings.h_fov / 2)
        LEFT = -RIGHT
        TOP = math.tan(view_settings.v_fov / 2)
        BOTTOM = -TOP
        THERE = math.tan(view_settings.d_fov / 2)
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