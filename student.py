from tkinter import Tk, Canvas, ARC, W
from hhhh import Human

class Student(Human):
    
    def __init__(self, canvas, name, x, y, gender, gr, var):
        super().__init__(canvas, name, x, y, gender)
        self.group = gr
        self.variant = var
        
    def _drawName(self):
        self.canvas.create_text(self.x-40, self.y-200, text = f'{self._name}, {self.group}, №{self.variant}', font = "Arial, 16", anchor = W, fill = "black")
