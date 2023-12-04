from tkinter import Tk, Canvas, ARC, SE, W
 
class Human():
 
    def __init__(self, canvas, name, x, y, gender):
        self.canvas = canvas
        self._name = name
        self.x = x
        self.y = y
        self.gender = gender
        
        
    def display(self):
        self._drawHead()
        self._drawBody()
        self._drawLeggs()
        self._drawHands()
        self._drawEye1()
        self._drawEye2()
        self._drawSmile()
        self._drawName()
        if self.gender == "м":
            self._drawPupil1M()
        elif self.gender == "ж":
            self._drawPupil1W()
        if self.gender == "м":
            self._drawPupil2M()
        elif self.gender == "ж":
            self._drawPupil2W()   
        if self.gender == "м":
            self._drawMan()
        elif self.gender == "ж":
            self._drawWoman()
        
    def _drawHead(self):
        self.canvas.create_oval(self.x+20, self.y-180, self.x+80, self.y-120, width = 2, fill = "beige")
        
    def _drawBody(self):
        self.canvas.create_line(self.x+50, self.y-120, self.x+50, self.y-50, width = 2)
        
    def _drawLeggs(self):
        self.canvas.create_line(self.x, self.y, self.x+50, self.y-50, self.x+100, self.y, width = 2)
    
    def _drawHands(self):
        self.canvas.create_line(self.x+10, self.y-70, self.x+50, self.y-110, self.x+90, self.y-70, width = 2)

    def _drawEye1(self):
        self.canvas.create_oval(self.x+35, self.y-165, self.x+45, self.y-155, width = 2, fill = "white")
    
    def _drawEye2(self):
        self.canvas.create_oval(self.x+55, self.y-165, self.x+65, self.y-155, width = 2, fill = "white")
        
    def _drawSmile(self):
        self.canvas.create_arc(self.x+40, self.y-150, self.x+60, self.y-135, width = 2, start = 0, extent =-180, fill = "red")
        
    def _drawName(self):
        self.canvas.create_text(self.x, self.y-220, text = self._name, font = "Arial, 16", anchor = W, fill = "black")
     
    def _drawPupil1M(self):
        self.canvas.create_oval(self.x+38, self.y-162, self.x+42, self.y-158, width = 2, fill = "blue")
    
    def _drawPupil1W(self):
        self.canvas.create_oval(self.x+38, self.y-162, self.x+42, self.y-158, width = 2, fill = "green")
    
    def _drawPupil2M(self):
        self.canvas.create_oval(self.x+58, self.y-162, self.x+62, self.y-158, width = 2, fill = "blue")
    
    def _drawPupil2W(self):
        self.canvas.create_oval(self.x+58, self.y-162, self.x+62, self.y-158, width = 2, fill = "green")
    
    def _drawMan(self):
        self.canvas.create_line(self.x+35, self.y-185, self.x+35, self.y-175, width = 2)
        self.canvas.create_line(self.x+50, self.y-190, self.x+50, self.y-180, width = 2)
        self.canvas.create_line(self.x+65, self.y-185, self.x+65, self.y-175, width = 2)
        
    def _drawWoman(self):
        self.canvas.create_line(self.x+35, self.y-175, self.x+10, self.y-160, width = 2)
        self.canvas.create_line(self.x+65, self.y-175, self.x+90, self.y-160, width = 2)

