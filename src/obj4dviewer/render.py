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
        self.scene.init_camera(camera)
        self.mouse_scroll_subj.attach(CameraMouseScrollObserver(self.scene.camera_controller, self.settings.mouse_factor, self.settings.mouse_speed))

    def draw_object(self, object:Object):
        vertices = object.vertices @ self.scene.camera.camera_matrix()
        vertices = vertices @ self.scene.camera.projection.matrix()
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.settings.screen_settings.screen_matrix
        vertices = vertices[:, :2]

        is_3d_obj = object.cells is None
        if object.face_normals is not None:
            face_normals = (object.face_normals-object.vertex_normals_origin) @ self.scene.camera.rotate_matrix()
        if object.cell_normals is not None:
            cell_normals = (object.cell_normals-object.vertex_normals_origin) @ self.scene.camera.rotate_matrix()
        
        for index, color_face in enumerate(object.color_faces):
            color, face = color_face
            cull = False
            if is_3d_obj:
                #backface cull
                if object.face_normals is not None:
                    cull = backface_cull(face_normals[index][:-1], np.array([0,0,1,0]))
            else:
                if object.cell_normals is not None:
                    # find which cell contains this face
                    for idx, c in enumerate(object.cells):
                        if index in c:
                            cull = backface_cull(cell_normals[idx][:-1], np.array([0,0,0,1]))
                
            polygon = vertices[face]
            if not cull and not any_func(polygon, self.settings.screen_settings.H_WIDTH, self.settings.screen_settings.H_HEIGHT, self.settings.screen_settings.H_DEPTH):
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

    def check_quit(self, key_to_quit = pg.K_ESCAPE):
        keypressed = pg.key.get_pressed()       
        if keypressed[key_to_quit]:
            exit()  
        
    def handle_pg_event(self):  
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEWHEEL:
                self.mouse_scroll_subj.update_scroll_direction((event.x, event.y))

    def run(self):
        while True:
            self.check_quit()
            self.draw_scene()
            self.scene.camera_controller.control()
            self.scene.camera_controller.mouse_input(self.settings.mouse_factor*self.settings.mouse_speed)
            self.handle_pg_event()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.settings.FPS)

def backface_cull(normal, view_direction) -> bool:
    dot = np.dot(normal, view_direction)
    return dot > 0