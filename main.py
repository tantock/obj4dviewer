from render import SoftwareRender
import math

if __name__ == '__main__':
    app = SoftwareRender()
    tesseract_id = app.load_object_from_file('resources/tesseract.obj4')
    tank_id = app.load_object_from_file('resources/t_34_obj.obj')
    app.get_object(tesseract_id).rotate_y(-math.pi / 4)
    app.get_object(tesseract_id).scale(10)
    app.get_object(tesseract_id).translate([10,10,10,0])
    app.get_object(tank_id).rotate_y(-math.pi / 4)
    app.get_object(tank_id).scale(1/5)
    app.run()