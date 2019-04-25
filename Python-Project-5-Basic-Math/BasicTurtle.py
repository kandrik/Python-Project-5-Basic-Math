from turtle import *

shape('turtle')

def square(side):
    for i in range(4):
        forward(side)
        right(90)

x = 5
for i in range(60):
    square(x)
    right(5)
    x += 5
