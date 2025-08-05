from obj4drender.object import *
from obj4drender.camera import *
from obj4drender.projection import *
from obj4drender.screen_settings import ScreenSettings
import pygame as pg

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.DEPTH = 1600
        self.H_WIDTH, self.H_HEIGHT, self.H_DEPTH = self.WIDTH // 2, self.HEIGHT // 2, self.DEPTH //2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.objects = {}
        self.autoincrement_obj_id = 0
        self.create_default_scene()

    def create_default_scene(self):
        self.camera = Camera(CameraViewSetting(math.pi / 3, 9/16, 1, 0.1, 100), [-5, 6, -55, 0])
        self.projection = Perspective(self.camera.view_settings)
        self.screen_settings = ScreenSettings(self)
    
    def load_object_from_file(self, filename) -> int:
        return self.add_object(self.get_object_from_file(filename))
    
    def add_object(self, object:Object) -> int:
        id = self.autoincrement_obj_id
        self.objects[id] = object
        self.autoincrement_obj_id += 1
        return id
    
    def pop_object(self, id:int) -> Object:
        return self.objects.pop(id)
    
    def get_object(self, id:int) -> Object:
        return self.objects[id]

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        extra_dim = [0, 1]
        if filename[-5:] == '.obj4':
            extra_dim = [1]
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + extra_dim)
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        for object in self.objects.values():
            object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
