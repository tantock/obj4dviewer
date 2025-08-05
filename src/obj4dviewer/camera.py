import pygame as pg
from obj4dviewer.matrix_functions import *
from obj4dviewer.camera_view_setting import CameraViewSetting
class Camera:
    def __init__(self, view_settings:CameraViewSetting, position):
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 0, 1])
        self.up = np.array([0, 1, 0, 0, 1])
        self.right = np.array([1, 0, 0, 0, 1])
        self.there = np.array([0, 0, 0, 1, 1])
        self.view_settings = view_settings
        self.moving_speed = 0.3
        self.rotation_speed = 0.015

        self.anglePitch = 0
        self.angleYaw = 0
        self.angleRoll = 0

        self.angleYawRoll = 0 #yz
        self.anglePitchRoll = 0 #xz
        self.anglePitchYaw = 0 #xy
        self.four_rotation = False

    def control(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position -= self.right * self.moving_speed
        if key[pg.K_d]:
            self.position += self.right * self.moving_speed
        if key[pg.K_w]:
            self.position += self.forward * self.moving_speed
        if key[pg.K_s]:
            self.position -= self.forward * self.moving_speed
        if key[pg.K_q]:
            self.position += self.up * self.moving_speed
        if key[pg.K_e]:
            self.position -= self.up * self.moving_speed
        if key[pg.K_SPACE]:
            self.position += self.there * self.moving_speed
        if key[pg.K_LCTRL]:
            self.position -= self.there * self.moving_speed

        if key[pg.K_LEFT]:
            self.four_rotation = False
            self.camera_yaw(-self.rotation_speed)
        if key[pg.K_RIGHT]:
            self.four_rotation = False
            self.camera_yaw(self.rotation_speed)
        if key[pg.K_UP]:
            self.four_rotation = False
            self.camera_pitch(-self.rotation_speed)
        if key[pg.K_DOWN]:
            self.four_rotation = False
            self.camera_pitch(self.rotation_speed)
        if key[pg.K_i]:
            self.four_rotation = True
            self.camera_PitchYaw(-self.rotation_speed)
        if key[pg.K_k]:
            self.four_rotation = True
            self.camera_PitchYaw(self.rotation_speed)
        if key[pg.K_j]:
            self.four_rotation = True
            self.camera_YawRoll(-self.rotation_speed)
        if key[pg.K_l]:
            self.four_rotation = True
            self.camera_YawRoll(self.rotation_speed)
        if key[pg.K_u]:
            self.four_rotation = True
            self.camera_PitchRoll(-self.rotation_speed)
        if key[pg.K_o]:
            self.four_rotation = True
            self.camera_PitchRoll(self.rotation_speed)

    def camera_yaw(self, angle):
        self.angleYaw += angle

    def camera_pitch(self, angle):
        self.anglePitch += angle

    def camera_YawRoll(self, angle): #yz
        self.angleYawRoll += angle

    def camera_PitchRoll(self, angle): #xz
        self.anglePitchRoll += angle

    def camera_PitchYaw(self, angle): #xy
        self.anglePitchYaw += angle    

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
        return self.translate_matrix() @ self.rotate_matrix()

    def translate_matrix(self):
        x, y, z, w, h = self.position
        return np.array([
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [-x, -y, -z, -w, 1]
        ])

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