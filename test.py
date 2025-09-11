import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

# t.forward(200)
# turtle.done()

def message (input):
    print(input)
message("hello class")

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)

def equaltri(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)

def righttri(x):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)

def star(x):
    t.forward(x)
    t.right(144)
    t.forward(x)
    t.right(144)
    t.forward(x)
    t.right(144)
    t.forward(x)
    t.right(144)
    t.forward(x)

def addstar(x):
    length = 5
    for i in range (x):
        star(length)
        length+= 10
        t.left(181)
        t.speed(10000)
    
addstar(60)

# for i in range(60):
#     square(100)
#     t.right(5)
#     t.speed(10000)

# def addSquares(iRange):
#     length = 5
#     for i in range(iRange):
#         square(length)
#         length += 5
#         t.right(5)
#         t.speed(10000)
# addSquares(60)

# def doubleSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length)
#         length = length * 2
# doubleSquares(10)

