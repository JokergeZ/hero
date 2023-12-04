from tkinter import Tk, Canvas, ARC, W
from weapon import Weapon

class Sword(Weapon):

    def __init__(self, c, n, d):
        self._canvas = c
        self._name = n
        self._damage = d
        
    def display(self, x, y):
        self._canvas.create_line(x+10, y-70, x-10, y-150, width = 2, fill = 'red')
        self._canvas.create_line(x-10, y-75, x+25, y-90, width = 2)
        pass
