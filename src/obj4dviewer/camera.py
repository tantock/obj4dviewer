import pygame as pg
from obj4dviewer.matrix_functions import *
class Camera:
    def __init__(self, position, projection):
        self.projection = projection
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 0, 1])
        self.up = np.array([0, 1, 0, 0, 1])
        self.right = np.array([1, 0, 0, 0, 1])
        self.there = np.array([0, 0, 0, 1, 1])
        self.moving_speed = 0.3
        self.rotation_speed = 0.015

        self.anglePitch = 0
        self.angleYaw = 0
        self.angleRoll = 0

        self.angleYawRoll = 0 #yz
        self.anglePitchRoll = 0 #xz
        self.anglePitchYaw = 0 #xy
        self.four_rotation = False

    def axiiIdentity(self):
        self.forward = np.array([0, 0, 1, 0, 1])
        self.up = np.array([0, 1, 0, 0, 1])
        self.right = np.array([1, 0, 0, 0, 1])
        self.there = np.array([0, 0, 0, 1, 1])

    def camera_update_axii(self):
        # rotate = rotate_y(self.angleYaw) @ rotate_x(self.anglePitch)
        if not self.four_rotation:
            rotate = rotate_x(self.anglePitch) @ rotate_y(self.angleYaw)  # this concatenation gives right visual
        else:
            rotate = rotate_xy(self.anglePitchYaw) @ rotate_yz(self.angleYawRoll) @ rotate_xz(self.anglePitchRoll)
        self.axiiIdentity()
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate
        self.there = self.there @ rotate

    def camera_matrix(self):
        self.camera_update_axii()
        return translate(-self.position[:-1]) @ self.rotate_matrix()

    def rotate_matrix(self):
        rx, ry, rz, rw, h = self.right
        fx, fy, fz, fw, h = self.forward
        ux, uy, uz, uw, h = self.up
        tx, ty, tz, tw, h = self.there
        return np.array([
            [rx, ux, fx, tx, 0],
            [ry, uy, fy, ty, 0],
            [rz, uz, fz, tz, 0],
            [rw, uw, fw, tw, 0],
            [0, 0, 0, 0, 1]
        ])