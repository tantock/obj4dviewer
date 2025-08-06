from obj4dviewer.object import *
from obj4dviewer.camera import *
from obj4dviewer.projection import *
from obj4dviewer.screen_setting import ScreenSetting
import pygame as pg

class SoftwareRender:
    def __init__(self, res_width, res_height, **kwargs):
        pg.init()
        self.screen_settings = ScreenSetting(res_width, res_height, kwargs.pop('res_depth', res_width))
        self.FPS = kwargs.pop('fps', 60)
        self.fov = math.radians(kwargs.pop('fov', 90))
        self.sky_colour = kwargs.pop('sky_colour', 'darkslategray')
        near_plane = kwargs.pop("near_clip", 0.1)
        far_plane = kwargs.pop("far_clip", 100)

        self.camera_view_settings = CameraViewSetting(self.fov, self.screen_settings.aspect_hw(), self.screen_settings.aspect_dw(), near_plane, far_plane)
        self.screen = pg.display.set_mode(self.screen_settings.RES())
        self.clock = pg.time.Clock()
        self.objects = {}
        self.autoincrement_obj_id = 0

        self.create_default_scene()

    def create_default_scene(self):
        self.camera = Camera(self.camera_view_settings, [-5, 6, -55, 0], Perspective(self.camera_view_settings))

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
        return Object(vertex, faces)

    def draw_object(self, object:Object):
        vertices = object.vertices @ self.camera.camera_matrix()
        vertices = vertices @ self.camera.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.screen_settings.screen_matrix
        vertices = vertices[:, :2]

        for index, color_face in enumerate(object.color_faces):
            color, face = color_face
            polygon = vertices[face]
            if not any_func(polygon, self.screen_settings.H_WIDTH, self.screen_settings.H_HEIGHT, self.screen_settings.H_DEPTH):
                pg.draw.polygon(self.screen, color, polygon, 1)
                if object.label:
                    text = object.font.render(object.label[index], True, pg.Color('white'))
                    self.screen.blit(text, polygon[-1])

        if object.draw_vertices:
            for vertex in vertices:
                if not any_func(vertex, self.screen_settings.H_WIDTH, self.screen_settings.H_HEIGHT, self.screen_settings.H_DEPTH):
                    pg.draw.circle(self.screen, pg.Color('white'), vertex, 2)

    def draw_scene(self):
        self.screen.fill(pg.Color(self.sky_colour))
        for object in self.objects.values():
            self.draw_object(object)

    def run(self):
        while True:
            self.draw_scene()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
