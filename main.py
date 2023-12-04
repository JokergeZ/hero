from tkinter import Tk, Canvas
from grid import Grid
from hero import Hero
from sword import Sword
from bow import Bow
import random

root = Tk()
canvas = Canvas(root, width = 800, height = 600)
canvas.pack()
grid = Grid(canvas)
grid.display()

f = open ('students.txt','r',encoding='utf-8')

students = []
for student in f:
    z = student.split(';')
    id = int(z[0])
    name = z[1]
    var = int (z[2])
    group ='ИП-22'
    gender = z[4]
    students.append({'id': id, 'full_name': name,'variant' : var, 'group' : group, 'gender' : gender})   

f.close()

wp1 = Sword(canvas, 'Арондит', 20)
wp2 = Bow(canvas, 'Алихард', 20)

s1 = random.choice(students)
name = f"{s1['full_name'].split()[0]} {s1['full_name'].split()[1][0]}. {s1['full_name'].split()[2][0]}"
p1 = Hero(canvas, name, 100, 300, s1['gender'])
p1.setWeapon(wp1)
p1.display()

s2 = random.choice(students)
name = f"{s2['full_name'].split()[0]} {s2['full_name'].split()[1][0]}. {s2['full_name'].split()[2][0]}"
p2 = Hero(canvas, name, 300, 500, s2['gender'])
p2.setWeapon(wp2)
p2.display()

while p1._health > 0 and p2._health > 0:
    if p1._health > 0:
        p1.attack(p2)
    else:       
        p2.attack(p1)

root.mainloop()
