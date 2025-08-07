from obj4dviewer.object import *
from obj4dviewer.camera import *
from obj4dviewer.projection import *
from obj4dviewer.render_settings import RenderSettings
import obj4dviewer.model_file_handler
import pygame as pg
import os

class SoftwareRender:
    def __init__(self, settings:RenderSettings):
        pg.init()
        self.settings = settings
        self.screen = pg.display.set_mode(self.settings.screen_settings.RES())
        self.clock = pg.time.Clock()
        self.objects = {}
        self.autoincrement_obj_id = 0

        self.create_default_scene()

    def create_default_scene(self):
        self.camera = Camera([-5, 6, -55, 0], Perspective(self.settings.camera_view_settings))

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
        file, file_extension = os.path.splitext(filename)
        obj = None
        match file_extension:
            case '.obj':
                obj = obj4dviewer.model_file_handler.handle_obj_file(filename)
            case '.obj4':
                obj = obj4dviewer.model_file_handler.handle_obj4_file(filename)
            case _:
                raise NotImplementedError(f"No handler for extension: {file_extension}")
        
        return obj

    def draw_object(self, object:Object):
        vertices = object.vertices @ self.camera.camera_matrix()
        vertices = vertices @ self.camera.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.settings.screen_settings.screen_matrix
        vertices = vertices[:, :2]

        for index, color_face in enumerate(object.color_faces):
            color, face = color_face
            polygon = vertices[face]
            if not any_func(polygon, self.settings.screen_settings.H_WIDTH, self.settings.screen_settings.H_HEIGHT, self.settings.screen_settings.H_DEPTH):
                pg.draw.polygon(self.screen, color, polygon, 1)
                if object.label:
                    text = object.font.render(object.label[index], True, pg.Color('white'))
                    self.screen.blit(text, polygon[-1])

        if object.draw_vertices:
            for vertex in vertices:
                if not any_func(vertex, self.settings.screen_settings.H_WIDTH, self.settings.screen_settings.H_HEIGHT, self.settings.screen_settings.H_DEPTH):
                    pg.draw.circle(self.screen, pg.Color('white'), vertex, self.settings.vertex_sz)

    def draw_scene(self):
        self.screen.fill(pg.Color(self.settings.sky_colour))
        for object in self.objects.values():
            self.draw_object(object)

    def run(self):
        while True:
            self.draw_scene()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.settings.FPS)
