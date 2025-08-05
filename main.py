from obj4dviewer.render import SoftwareRender
from obj4dviewer.object import Axes4
import math

if __name__ == '__main__':
    app = SoftwareRender(1600,900)
    tesseract_id = app.load_object_from_file('resources/tesseract.obj4')
    tank_id = app.load_object_from_file('resources/t_34_obj.obj')
    axis_id = app.add_object(Axes4(app))
    
    tesseract = app.get_object(tesseract_id)
    tesseract.rotate_y(-math.pi / 4)
    tesseract.scale(10)
    tesseract.translate([10,10,10,0])
    
    tank = app.get_object(tank_id)
    tank.rotate_y(-math.pi / 4)
    tank.scale(1/5)
    
    app.run()