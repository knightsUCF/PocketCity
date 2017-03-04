import pygame
import log

io = log.log()
io.o('test')

class grid():
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.WHITE = (0, 2, 2)

        self.WIDTH = 100
        self.HEIGHT = 100

        self.GameGrid = []


    def Initialize(self):
        io.o('initializing grid\n')
        return 
    def GenerateGrid(self):
        io.o('generating grid\n')
        return 
    def UpdateGrid(self):
        io.o('updating grid')
        return 


    def Run(self):
        self.Initialize()
        self.GenerateGrid()
        self.UpdateGrid()











