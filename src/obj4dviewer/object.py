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

    def local_matrix_transform(self, matrix):
        return  translate(-self.position[:-1]) @ matrix @ translate(self.position[:-1])
    
    def transform(self, transform_matrix, world_space = False):
        if world_space:
            self.vertices = self.vertices @ transform_matrix
            self.position = self.position @ transform_matrix
        else:
            self.vertices = self.vertices @ self.local_matrix_transform(transform_matrix)

    def translate(self, pos, world_space = True):
        translate_matrix = translate(pos)
        self.transform(translate_matrix, world_space)

    def scale(self, scale_factor, world_space = False):
        scale_matrix = scale(scale_factor)
        self.transform(scale_matrix, world_space)

    def rotate_x(self, angle, world_space = False):
        rotate_matrix = rotate_x(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_y(self, angle, world_space = False):
        rotate_matrix = rotate_y(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_z(self, angle, world_space = False):
        rotate_matrix = rotate_z(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_zw(self, angle, world_space = False):
        rotate_matrix = rotate_zw(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_yw(self, angle, world_space = False):
        rotate_matrix = rotate_yw(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_yz(self, angle, world_space = False):
        rotate_matrix = rotate_yz(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_xw(self, angle, world_space = False):
        rotate_matrix = rotate_xw(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_xz(self, angle, world_space = False):
        rotate_matrix = rotate_xz(angle)
        self.transform(rotate_matrix, world_space)

    def rotate_xy(self, angle, world_space = False):
        rotate_matrix = rotate_xy(angle)
        self.transform(rotate_matrix, world_space)

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