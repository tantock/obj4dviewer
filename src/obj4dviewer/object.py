import pygame as pg
from obj4dviewer.matrix_functions import *
from numba import njit


@njit(fastmath=True)
def any_func(arr, a, b, c):
    return np.any((arr == a) | (arr == b) | (arr == c))


class Object:
    def __init__(self, vertices='', faces='', colour = 'orange'):
        self.vertices = np.array(vertices)
        self.position = np.array([0,0,0,0,1])
        self.faces = faces

        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_faces = [(pg.Color(colour), face) for face in self.faces]
        self.draw_vertices = False
        self.label = ''

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

    def rotate_zw(self, angle):
        self.vertices = self.vertices @ rotate_zw(angle)

    def rotate_yw(self, angle):
        self.vertices = self.vertices @ rotate_yw(angle)

    def rotate_yz(self, angle):
        self.vertices = self.vertices @ rotate_yz(angle)

    def rotate_xw(self, angle):
        self.vertices = self.vertices @ rotate_xw(angle)

    def rotate_xz(self, angle):
        self.vertices = self.vertices @ rotate_xz(angle)

    def rotate_xy(self, angle):
        self.vertices = self.vertices @ rotate_xy(angle)

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