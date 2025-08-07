from obj4dviewer.screen_settings import ScreenSettings
from obj4dviewer.camera_view_settings import CameraViewSettings
import math

class RenderSettings:
    def __init__(self, res_width, res_height, **kwargs):
        self.screen_settings = ScreenSettings(res_width, res_height, kwargs.pop('res_depth', res_width))
        self.FPS = kwargs.pop('fps', 60)
        self.fov = math.radians(kwargs.pop('fov', 90))
        self.sky_colour = kwargs.pop('sky_colour', 'darkslategray')
        near_plane = kwargs.pop("near_clip", 0.1)
        far_plane = kwargs.pop("far_clip", 100)
        self.vertex_sz = kwargs.pop("vertex_sz", 1)

        self.camera_view_settings = CameraViewSettings(self.fov, self.screen_settings.aspect_hw(), self.screen_settings.aspect_dw(), near_plane, far_plane)
        self.visible_mouse = kwargs.pop('visible_mouse', False)
        self.set_grab = not kwargs.pop('visible_mouse', False)
        self.mouse_factor = kwargs.pop('mouse_factor', 0.001)
        self.mouse_speed = kwargs.pop('mouse_speed', 0.5)