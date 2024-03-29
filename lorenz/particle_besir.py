import numpy as np
import pygame as pg
import ctypes


dimensions = (1000,1000)
screen = pg.display.set_mode(dimensions)

class Particle:
    def __init__(self, t, coords, scale):
        pg.init()
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.screen = pg.display.set_mode(dimensions)
        self.t = t
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.scale = scale
        self.xproj = 0
        self.yproj = 0
        self.zproj = 0
        self.o = 15
        self.rho = 28
        self.B = 8 / 3
    
    def calc(self):
        dx = (self.o * (self.y - self.x)) * self.t
        self.x = self.x + dx

        dy = ((self.x * (self.rho - self.z)) - self.y) * self.t
        self.y = self.y + dy

        dz = ((self.x * self.y) - (self.B * self.z)) * self.t
        self.z = self.z + dz

    # def rotateX(self, angle):
    #     x, y, z = self.x, self.y, self.z
    #     point = np.array([x, y, z])
    #     rotateX = np.matrix(
    #         [[1, 0, 0],
    #         [0, np.cos(angle), np.sin(angle)],
    #         [0, -np.sin(angle), np.cos(angle)]]
    #     )
    #     rotated = np.dot(rotateX, point)
    #     rotated = rotated.tolist()
    #     rotated = [rotated[0][0], rotated[0][1], rotated[0][2]]
    #     self.xproj, self.yproj, self.zproj = rotated

    def rotateX(self, angle):
        x, y, z = self.x, self.y, self.z
        point = np.array([x, y, z])
        rotateX = np.matrix(
            [[1, 0, 0],
            [0, np.cos(angle), np.sin(angle)],
            [0, -np.sin(angle), np.cos(angle)]]
        )
        rotated = np.dot(rotateX, point)
        self.xproj, self.yproj, self.zproj = rotated[0,0], rotated[0,1], rotated[0,2]


    def rotateY(self, angle):
        x, y, z = self.x, self.y, self.z
        point = np.array([x, y, z])
        rotateY = np.matrix(
        [[np.cos(angle), 0, -np.sin(angle)],
        [0, 1, 0],
        [np.sin(angle), 0, np.cos(angle)]]
        )
        rotated = np.dot(rotateY, point)
        rotated = rotated.tolist()
        rotated = [rotated[0][0], rotated[0][1], rotated[0][2]]
        self.xproj, self.yproj, self.zproj = rotated

    def rotateZ(self, angle):
        x, y, z = self.x, self.y, self.z
        point = np.array([x, y, z])
        rotateZ = np.matrix(
            [[np.cos(angle), np.sin(angle), 0],
            [-np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]]
        )
        rotated = np.dot(rotateZ, point)
        rotated = rotated.tolist()
        rotated = [rotated[0][0], rotated[0][1], rotated[0][2]]
        self.xproj, self.yproj, self.zproj = rotated

    # def project(self):
    #     x, y, z = self.xproj, self.yproj, self.zproj
    #     point = np.array([x, y, z])
    #     P = np.matrix(
    #         [[1, 0, 0],
    #         [0, 1, 0],
    #         [0, 0, 0]]
    #     )
    #     projected = np.dot(point, P)
    #     projected = projected.tolist()
    #     self.xproj = projected[0][0]
    #     self.yproj = projected[0][1]
    #     x = (self.xproj * self.scale) + (self.width // 2)
    #     y = (self.yproj * self.scale) + (self.height // 2)
    #     return (x, y)
    
    def project(self):
        x = (self.xproj * self.zproj) + (self.width // 2)
        y = (self.yproj * self.zproj) + (self.height // 2)
        return (x, y)