from tkinter import Tk, Canvas, ARC, W
from weapon import Weapon

class Bow(Weapon):

    def __init__(self, c, n, d):
        self._canvas = c
        self._name = n
        self._damage = d
        
    def display(self, x, y):
        self._canvas.create_arc(x+70, y-110, x+120, y-40, width = 2, start = 45, extent =-180)
        self._canvas.create_line(x+90, y-75, x+140, y-45, width = 2, fill = 'orange')
        self._canvas.create_line(x+130, y-55, x+140, y-45, x+127, y-45, width = 2, fill = 'gray')
        pass
