import numpy as np

class ScreenSetting():
    def __init__(self, WIDTH, HEIGHT, DEPTH):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.DEPTH = DEPTH
        self.H_WIDTH = WIDTH // 2
        self.H_HEIGHT = HEIGHT // 2
        self.H_DEPTH = DEPTH // 2

        HW, HH, HD = self.H_WIDTH, self.H_HEIGHT, self.H_DEPTH
        self.screen_matrix = np.array([
            [HW, 0, 0, 0, 0],
            [0, -HH, 0, 0, 0],
            [0, 0, HD, 0, 0],
            [0, 0, 0, 1, 0],
            [HW, HH, HD, 0, 1]
        ])

    def RES(self):
        return (self.WIDTH, self.HEIGHT)
    
    def aspect_hw(self):
        return self.HEIGHT/self.WIDTH
    
    def aspect_dw(self):
        return self.DEPTH/self.WIDTH