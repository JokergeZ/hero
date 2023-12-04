from tkinter import Tk, Canvas, ARC, W
from hhhh import Human

class Hero(Human):

    def __init__(self, canvas, name, x, y, gender):
        super().__init__(canvas, name, x, y, gender)
        self._health = 100
        self._wp = None
        self.health_bar_width = 100
        self.health_bar_height = 10
        self.health_bar_x = self.x + 1.5
        self.health_bar_y = self.y - 200
        self.health_bar2_y = self.y - 200
        self.health_bar_color = "red"
        self.dead_color = "white"

    def setWeapon(self, weapon):
        self._wp = weapon

    def attack(self, enemy):
        damage = self._wp.hit()
        enemy._health -= damage
        print(f'{self._name} нанес{"ла" if self.gender=="ж" else ""} {damage} урона {enemy._name}!')
        print(f'У {enemy._name} осталось {enemy._health} здоровья')

    def _drawName(self):
        super()._drawName()
        self.canvas.create_rectangle(self.health_bar_x,
                                     self.health_bar_y,
                                     self.health_bar_x + 100,
                                     self.health_bar_y + self.health_bar_height,
                                     fill=self.dead_color)
        self.canvas.create_rectangle(self.health_bar_x,
                                     self.health_bar_y,
                                     self.health_bar_x + self._health,
                                     self.health_bar2_y + self.health_bar_height,
                                     fill=self.health_bar_color)
    def _drawWeapon(self):
        self._wp.display(self.x, self.y)

    def display(self):
        super().display()
        self._drawWeapon()
