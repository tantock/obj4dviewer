from obj4dviewer.camera import Camera
import pygame as pg
class CameraController:
    def __init__(self, camera:Camera):
        self.camera = camera

    def control(self):
        key = pg.key.get_pressed()
        if key[pg.K_LSHIFT]:
            self.camera.axiiIdentity()
        if key[pg.K_a]:
            self.camera.position -= self.camera.right * self.camera.moving_speed
        if key[pg.K_d]:
            self.camera.position += self.camera.right * self.camera.moving_speed
        if key[pg.K_w]:
            self.camera.position += self.camera.forward * self.camera.moving_speed
        if key[pg.K_s]:
            self.camera.position -= self.camera.forward * self.camera.moving_speed
        if key[pg.K_q]:
            self.camera.position += self.camera.there * self.camera.moving_speed
        if key[pg.K_e]:
            self.camera.position -= self.camera.there * self.camera.moving_speed
        if key[pg.K_SPACE]:
            self.camera.position += self.camera.up * self.camera.moving_speed
        if key[pg.K_LCTRL]:
            self.camera.position -= self.camera.up * self.camera.moving_speed

        if key[pg.K_LEFT]:
            self.camera.four_rotation = False
            self.camera_yaw(-self.camera.rotation_speed)
        if key[pg.K_RIGHT]:
            self.camera.four_rotation = False
            self.camera_yaw(self.camera.rotation_speed)
        if key[pg.K_UP]:
            self.camera.four_rotation = False
            self.camera_pitch(-self.camera.rotation_speed)
        if key[pg.K_DOWN]:
            self.camera.four_rotation = False
            self.camera_pitch(self.camera.rotation_speed)
        if key[pg.K_i]:
            self.camera.four_rotation = True
            self.camera_PitchYaw(-self.camera.rotation_speed)
        if key[pg.K_k]:
            self.four_rotation = True
            self.camera_PitchYaw(self.camera.rotation_speed)
        if key[pg.K_j]:
            self.four_rotation = True
            self.camera_YawRoll(-self.camera.rotation_speed)
        if key[pg.K_l]:
            self.four_rotation = True
            self.camera_YawRoll(self.camera.rotation_speed)
        if key[pg.K_u]:
            self.camera.four_rotation = True
            self.camera_PitchRoll(-self.camera.rotation_speed)
        if key[pg.K_o]:
            self.camera.four_rotation = True
            self.camera_PitchRoll(self.camera.rotation_speed)

    def camera_yaw(self, angle):
        self.camera.angleYaw += angle

    def camera_pitch(self, angle):
        self.camera.anglePitch += angle

    def camera_YawRoll(self, angle): #yz
        self.camera.angleYawRoll += angle

    def camera_PitchRoll(self, angle): #xz
        self.camera.anglePitchRoll += angle

    def camera_PitchYaw(self, angle): #xy
        self.camera.anglePitchYaw += angle    

    def mouse_input(self, mouse_factor:float):
        self.camera.four_rotation = True
        delta_x, delta_y = pg.mouse.get_rel()
        rotation_direction_x = float(delta_x)*mouse_factor
        rotation_direction_y = -float(delta_y)*mouse_factor
        self.camera_PitchYaw(rotation_direction_y)
        self.camera_YawRoll(rotation_direction_x)