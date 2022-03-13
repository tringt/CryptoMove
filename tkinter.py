import tkinter
import random
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()



a = random.randint(-10, 10)
b = random.randint(-10, 10)


x111 = random.randint(0, 390)
y111 = random.randint(0, 390)


while True:
    x222 = random.randint(0, 390)
    if x222 % 2 == 0:
        break
while True:
    y222 = random.randint(0, 390)
    if y222 % 2 == 0:
        break


while True:
    x333 = random.randint(0, 390)
    if x333 % 3 == 0:
        break
while True:
    y333 = random.randint(0, 390)
    if y333 % 3 == 0:
        break


while True:
    x444 = random.randint(0, 390)
    if x444 % 4 == 0:
        break
while True:
    y444 = random.randint(0, 390)
    if y444 % 4 == 0:
        break


while True:
    x555 = random.randint(0, 390)
    if x555 % 5 == 0:
        break
while True:
    y555 = random.randint(0, 390)
    if y555 % 5 == 0:
        break




roma1 = canvas.create_oval(x111, y111, x111+25, y111+25, fill='purple')
roma2 = canvas.create_oval(x222, y222, x222+20, y222+20, fill='red')
roma3 = canvas.create_oval(x333, y333, x333+10, y333+10, fill='blue')
roma4 = canvas.create_oval(x444, y444, x444+16, y444+16, fill='yellow')
roma5 = canvas.create_oval(x555, y555, x555+30, y555+30, fill='green')









l = 1
m = 1
n = 2
o = 1
p = 0
q = 3
r = 4
s = 4
t = 5
u = 5


while True:

    x0_1, y0_1, x1_1, y1_1 = canvas.coords(roma1)
    x0_2, y0_2, x1_2, y1_2 = canvas.coords(roma2)
    x0_3, y0_3, x1_3, y1_3 = canvas.coords(roma3)
    x0_4, y0_4, x1_4, y1_4 = canvas.coords(roma4)    
    x0_5, y0_5, x1_5, y1_5 = canvas.coords(roma5)

    if x0_1 == 400 or x0_1 == 0:
        l = -l
    if y0_1 == 0 or y0_1 == 400:
        m = -m
    if x1_1 == 400 or x1_1 == 0:
        l = -l
    if y1_1 == 0 or y1_1 == 400:
        m = -m


    if x0_2 == 400 or x0_2 == 0:
        n = -n
    if y0_2 == 0 or y0_2 == 400:
        o = -o
    if x1_2 == 400 or x1_2 == 0:
        n = -n
    if y1_2 == 0 or y1_2 == 400:
        o = -o


    if x0_3 == 400 or x0_3 == 0:
        p = -p
    if y0_3 == 0 or y0_3 == 400:
        q = -q
    if x1_3 == 400 or x1_3 == 0:
        p = -p
    if y1_3 == 0 or y1_3 == 400:
        q = -q


    if x0_4 == 400 or x0_4 == 0:
        r = -r
    if y0_4 == 0 or y0_4 == 400:
        s = -s
    if x1_4 == 400 or x1_4 == 0:
        r = -r
    if y1_4 == 0 or y1_4 == 400:
        s = -s


    if x0_5 == 400 or x0_5 == 0:
        t = -t
    if y0_5 == 0 or y0_5 == 400:
        u = -u
    if x1_5 == 400 or x1_5 == 0:
        t = -t
    if y1_5 == 0 or y1_5 == 400:
        u = -u





    canvas.move(roma1, l, m)
    canvas.move(roma2, n, o)
    canvas.move(roma3, p, q)
    canvas.move(roma4, r, s)
    canvas.move(roma5, t, u)

    canvas.update()


canvas.mainloop()
