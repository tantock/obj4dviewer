import math
import numpy as np


def translate(pos):
    tx, ty, tz, tw = pos
    return np.array([
        [1,  0,  0,  0,  0],
        [0,  1,  0,  0,  0],
        [0,  0,  1,  0,  0],
        [0,  0,  0,  1,  0],
        [tx, ty, tz, tw, 1]
    ])


def rotate_x(a):
    return np.array([
        [1, 0, 0, 0, 0],
        [0, math.cos(a), math.sin(a), 0, 0],
        [0, -math.sin(a), math.cos(a), 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ])


def rotate_y(a):
    return np.array([
        [math.cos(a), 0, -math.sin(a), 0, 0],
        [0, 1, 0, 0, 0],
        [math.sin(a), 0, math.cos(a), 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ])


def rotate_z(a):
    return np.array([
        [math.cos(a), math.sin(a), 0, 0, 0],
        [-math.sin(a), math.cos(a), 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ])


def scale(n):
    return np.array([
        [n, 0, 0, 0, 0],
        [0, n, 0, 0, 0],
        [0, 0, n, 0, 0],
        [0, 0, 0, n, 0],
        [0, 0, 0, 0, 1]
    ])

def rotate_zw(a):
    return np.array([
        [math.cos(a),  math.sin(a),  0,  0,  0],
        [-math.sin(a),  math.cos(a),  0,  0,  0],
        [0,  0,  1,  0,  0],
        [0,  0,  0,  1,  0],
        [0,  0,  0,  0,  1]
    ])

def rotate_yw(a):
    return np.array([
        [math.cos(a),  0,  math.sin(a),  0,  0],
        [0,  1,  0,  0,  0],
        [-math.sin(a),  0,  math.cos(a),  0,  0],
        [0,  0,  0,  1,  0],
        [0,  0,  0,  0,  1]
    ])

def rotate_yz(a):
    return np.array([
        [math.cos(a),  0,  0,  math.sin(a),  0],
        [0,  1,  0,  0,  0],
        [0,  0,  1,  0,  0],
        [-math.sin(a),  0,  0,  math.cos(a),  0],
        [0,  0,  0,  0,  1]
    ])

def rotate_xw(a):
    return np.array([
        [1,  0,  0,  0,  0],
        [0,  math.cos(a),  math.sin(a),  0,  0],
        [0,  -math.sin(a),  math.cos(a),  0,  0],
        [0,  0,  0,  1,  0],
        [0,  0,  0,  0,  1]
    ])

def rotate_xz(a):
    return np.array([
        [1,  0,  0,  0,  0],
        [0,  math.cos(a),  0,  math.sin(a),  0],
        [0,  0,  1,  0,  0],
        [0,  -math.sin(a),  0,  math.cos(a),  0],
        [0,  0,  0,  0,  1]
    ])

def rotate_xy(a):
    return np.array([
        [1,  0,  0,  0,  0],
        [0,  1,  0,  0,  0],
        [0,  0,  math.cos(a),  math.sin(a),  0],
        [0,  0,  -math.sin(a),  math.cos(a),  0],
        [0,  0,  0,  0,  1]
    ])

def cross4(U,V,W):
    A = (V[0] * W[1]) - (V[1] * W[0])
    B = (V[0] * W[2]) - (V[2] * W[0])
    C = (V[0] * W[3]) - (V[3] * W[0])
    D = (V[1] * W[2]) - (V[2] * W[1])
    E = (V[1] * W[3]) - (V[3] * W[1])
    F = (V[2] * W[3]) - (V[3] * W[2])
    
    result = []

    result.append( (U[1] * F) - (U[2] * E) + (U[3] * D))
    result.append(-(U[0] * F) + (U[2] * C) - (U[3] * B))
    result.append( (U[0] * E) - (U[1] * C) + (U[3] * A))
    result.append(-(U[0] * D) + (U[1] * B) - (U[2] * A))

    return np.array(result)
