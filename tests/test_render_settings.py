from obj4dviewer.render_settings import *

def test_init():

    settings = RenderSettings(1920, 1080, 
                              res_depth = 1280, fps = 45, fov = 75,
                              sky_colour = 'blue', near_clip = 10, far_clip = 100,
                              vertex_sz = 10, visible_mouse = True, mouse_factor = 0.1, 
                              mouse_speed = 2)

    assert (settings.screen_settings.WIDTH, settings.screen_settings.HEIGHT , settings.screen_settings.DEPTH) == (1920, 1080, 1280)
    assert settings.FPS == 45
    assert settings.fov == math.radians(75)
    assert settings.sky_colour == 'blue'
    assert settings.vertex_sz == 10

    assert settings.camera_view_settings == CameraViewSettings(75, 1080/1920, 1280/1920, 10, 100)
    assert settings.visible_mouse == True
    assert settings.set_grab == False
    assert settings.mouse_factor == 0.1
    assert settings.mouse_speed == math.log(max(0, 2)+1)