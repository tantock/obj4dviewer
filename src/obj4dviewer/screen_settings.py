import numpy as np
class ScreenSettings:
    def __init__(self, render):
        HW, HH, HD = render.H_WIDTH, render.H_HEIGHT, render.H_DEPTH
        self.to_screen_matrix = np.array([
            [HW, 0, 0, 0, 0],
            [0, -HH, 0, 0, 0],
            [0, 0, HD, 0, 0],
            [0, 0, 0, 1, 0],
            [HW, HH, HD, 0, 1]
        ])