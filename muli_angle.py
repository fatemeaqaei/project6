import turtle
import random

n = 3 
p = turtle.Pen()


while n >= 3:
    black = random.randint(0,255)
    p.pencolor(black/255, black/255, black/255)

    zavie = (n - 2) * 180 / n
    
    p.left(180-zavie/2)
    
    for i in range(n):
        p.forward(50 * (1+ n/10))
        p.left(180-zavie)
        
    
    p.right(180-zavie/2)
    p.penup()
    p.forward(9* (1+ n/10))
    p.pendown()
    n += 1
    