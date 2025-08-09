from dataclasses import dataclass

@dataclass
class CameraViewSettings:
    def __init__(self, h_fov:float, aspect_hw:float, aspect_dw:float, near_clip:float, far_clip:float):
        self.h_fov = h_fov # horizontal field of view
        self.v_fov = self.h_fov * aspect_hw # vertical field of view
        self.d_fov = self.h_fov * aspect_dw # depth field of view
        self.near_plane = near_clip
        self.far_plane = far_clip