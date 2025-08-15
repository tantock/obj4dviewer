from obj4dviewer.render import SoftwareRender
from obj4dviewer.render_settings import RenderSettings
from obj4dviewer.object import Axes4
import math

if __name__ == '__main__':
    app = SoftwareRender(RenderSettings(1600, 900, sky_colour = 'black'))
    tesseract_id = app.scene.load_object_from_file('resources/tesseract.obj4')
    teapot_id = app.scene.load_object_from_file('resources/teapot.obj')
    axis_hint_id = app.scene.load_object_from_file('resources/axis_hint.obj4')
    axis_id = app.scene.add_object(Axes4())
    
    tesseract = app.scene.get_object(tesseract_id)
    tesseract.rotate_y(-math.pi / 4)
    tesseract.scale(10)
    tesseract.translate([10,0,10,0])
    
    teapot = app.scene.get_object(teapot_id)
    teapot.rotate_y(-math.pi / 4)
    teapot.translate([-10,0,-10,0])
    teapot.scale(2)

    axis = app.scene.get_object(axis_id)
    axis.scale(5)

    axis_hint = app.scene.get_object(axis_hint_id)
    axis_hint.backface_cull_enable = False
    
    app.run()