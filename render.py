from object import *
from camera import *
from projection import *
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
        self.objects = []
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [-5, 6, -55, 0])
        self.projection = Projection(self)
        self.objects.append(self.get_object_from_file('resources/tesseract.obj4'))
        self.objects[-1].rotate_y(-math.pi / 4)
        self.objects[-1].scale(10)
        self.objects[-1].translate([10,10,10,0])

        self.objects.append(self.get_object_from_file('resources/t_34_obj.obj'))
        self.objects[-1].rotate_y(-math.pi / 4)
        self.objects[-1].scale(1/5)

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
        for object in self.objects:
            object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
