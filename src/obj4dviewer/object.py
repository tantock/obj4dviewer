import pygame as pg
from obj4dviewer.matrix_functions import *
from numba import njit


@njit(fastmath=True)
def any_func(arr, a, b, c):
    return np.any((arr == a) | (arr == b) | (arr == c))


class Object:
    def __init__(self, vertices='', faces='', colour = 'orange'):
        self.vertices = np.array(vertices)
        self.faces = faces
        self.translate([0.0001, 0.0001, 0.0001, 0.0001])

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color(colour), face) for face in self.faces]
        self.draw_vertices = False
        self.label = ''

    def draw(self, renderer):
        self.screen_projection(renderer)

    def screen_projection(self, renderer):
        vertices = self.vertices @ renderer.camera.camera_matrix()
        vertices = vertices @ renderer.camera.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ renderer.screen_settings.screen_matrix
        vertices = vertices[:, :2]

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertices[face]
            if not any_func(polygon, renderer.screen_settings.H_WIDTH, renderer.screen_settings.H_HEIGHT, renderer.screen_settings.H_DEPTH):
                pg.draw.polygon(renderer.screen, color, polygon, 1)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    renderer.screen.blit(text, polygon[-1])

        if self.draw_vertices:
            for vertex in vertices:
                if not any_func(vertex, renderer.H_WIDTH, renderer.H_HEIGHT, renderer.H_DEPTH):
                    pg.draw.circle(renderer.screen, pg.Color('white'), vertex, 2)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)


class Axes3(Object):
    def __init__(self):
        super().__init__(vertices=np.array([(0, 0, 0, 0, 1), (1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (0, 0, 1, 0, 1)]))
        self.faces = np.array([(0, 1), (0, 2), (0, 3)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertices = False
        self.label = 'XYZ'

class Axes4(Object):
    def __init__(self):
        super().__init__(vertices=np.array([(0, 0, 0, 0, 1), (1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (0, 0, 1, 0, 1), (0, 0, 0, 1, 1)]))
        self.faces = np.array([(0, 1), (0, 2), (0, 3), (0, 4)])
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue'), pg.Color('yellow')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertices = False
        self.label = 'XYZW'