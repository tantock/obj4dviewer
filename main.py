from obj4dviewer.render import SoftwareRender
from obj4dviewer.render_settings import RenderSettings
from obj4dviewer.object import Axes4
import math

if __name__ == '__main__':
    app = SoftwareRender(RenderSettings(1600, 900))
    tesseract_id = app.scene.load_object_from_file('resources/tesseract.obj4')
    tank_id = app.scene.load_object_from_file('resources/t_34_obj.obj')
    axis_id = app.scene.add_object(Axes4())
    
    tesseract = app.scene.get_object(tesseract_id)
    tesseract.rotate_y(-math.pi / 4)
    tesseract.scale(10)
    tesseract.translate([10,10,10,0])
    
    tank = app.scene.get_object(tank_id)
    tank.rotate_y(-math.pi / 4)
    tank.scale(1/5)
    
    app.run()