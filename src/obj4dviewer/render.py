from obj4dviewer.object import *
from obj4dviewer.camera import *
from obj4dviewer.projection import *
from obj4dviewer.render_settings import RenderSettings
from obj4dviewer.scene import Scene
from obj4dviewer.mouse_event_subj_obs import CameraMouseScrollObserver, MouseScrollSubject
import pygame as pg

class SoftwareRender:
    def __init__(self, settings:RenderSettings):
        pg.init()
        self.settings = settings
        self.screen = pg.display.set_mode(self.settings.screen_settings.RES())
        pg.mouse.set_visible(settings.visible_mouse)
        pg.event.set_grab(settings.set_grab)

        self.clock = pg.time.Clock()
        self.scene = Scene()
        self.mouse_scroll_subj = MouseScrollSubject()
        self.add_camera_to_scene()

    def add_camera_to_scene(self):
        camera = Camera([-5, 6, -55, 0], Perspective(self.settings.camera_view_settings))
        self.scene.init_camera(camera, self.settings.mouse_speed, self.settings.mouse_factor)
        self.mouse_scroll_subj.attach(CameraMouseScrollObserver(self.scene.camera_controller))

    def draw_object(self, object:Object):
        vertices = object.vertices @ self.scene.camera.camera_matrix()
        vertices = vertices @ self.scene.camera.projection.projection_matrix
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
        for object in self.scene.objects.values():
            self.draw_object(object)

    def run(self):
        while True:
            self.draw_scene()
            self.scene.camera_controller.control()
            self.scene.camera_controller.mouse_input(self.settings.mouse_factor*self.settings.mouse_speed)
                
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.MOUSEWHEEL:
                    self.mouse_scroll_subj.update_scroll_direction((event.x, event.y))
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.settings.FPS)
