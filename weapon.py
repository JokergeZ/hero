from tkinter import Tk, Canvas, ARC, W
from random import randrange

class Weapon():

    def __init__(self,c, n, d):
        self._canvas = c
        self._name = n
        self._damage = d

    def display(self, x, y):
        pass
    
    def hit(self):
        damage = randrange(self._damage-5, self._damage+5)
        return damage
