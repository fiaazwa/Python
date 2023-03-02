from turtle import *

color('cyan')
bgcolor('black')
speed(11)
right(45)
for n in range(150):
    if 7<n<62:
        left(5)
    if 80<n<133:
        right(5)
    circle(30)
    if n<80:
        forward(10)
    else:
        forward(5)
   

# from turtle import *

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) <1:
#         break
# end_fill()
# done()

# from turtle import *
# # Set initial position
# penup ()
# left (90)
# fd (200)
# pendown ()
# right (90)
 
# # flower base
# fillcolor ("red")
# begin_fill ()
# circle (10,180)
# circle (25,110)
# left (50)
# circle (60,45)
# circle (20,170)
# right (24)
# fd (30)
# left (10)
# circle (30,110)
# fd (20)
# left (40)
# circle (90,70)
# circle (30,150)
# right (30)
# fd (15)
# circle (80,90)
# left (15)
# fd (45)
# right (165)
# fd (20)
# left (155)
# circle (150,80)
# left (50)
# circle (150,90)
# end_fill ()
 
# # Petal 1
# left (150)
# circle (-90,70)
# left (20)
# circle (75,105)
# setheading (60)
# circle (80,98)
# circle (-90,40)
 
# # Petal 2
# left (180)
# circle (90,40)
# circle (-80,98)
# setheading (-83)
 
# # Leaves 1
# fd (30)
# left (90)
# fd (25)
# left (45)
# fillcolor ("green")
# begin_fill ()
# circle (-80,90)
# right (90)
# circle (-80,90)
# end_fill ()
# right (135)
# fd (60)
# left (180)
# fd (85)
# left (90)
# fd (80)
 
# # Leaves 2
# right (90)
# right (45)
# fillcolor ("green")
# begin_fill ()
# circle (80,90)
# left (90)
# circle (80,90)
# end_fill ()
# left (135)
# fd (60)
# left (180)
# fd (60)
# right (90)
# circle (200,60)
# done()

# import math
 
# # Set the background color
# screen = Screen()
# screen.bgcolor("lightpink")
 
# # Create our turtle
# t =Turtle()
# t.color("black")
# t.shape("turtle")
# t.speed(5)
 
# # Define a function to draw and
# # fill a rectangle with the given
# # dimensions and color
# def drawRectangle(t, width, height, color):
   
#     t.fillcolor(color)
#     t.begin_fill()
#     t.forward(width)
#     t.left(90)
#     t.forward(height)
#     t.left(90)
#     t.forward(width)
#     t.left(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
 
 
# # Define a function to draw and fill an equalateral right
# # triangle with the given hypotenuse length and color.  This
# # is used to create a roof shape.
# def drawTriangle(t, length, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     t.forward(length)
#     t.left(135)
#     t.forward(length / math.sqrt(2))
#     t.left(90)
#     t.forward(length / math.sqrt(2))
#     t.left(135)
#     t.end_fill()
 
 
# # Define a function to draw and fill a parallelogram, used to
# # draw the side of the house
# def drawParallelogram(t, width, height, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     t.left(30)
#     t.forward(width)
#     t.left(60)
#     t.forward(height)
#     t.left(120)
#     t.forward(width)
#     t.left(60)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
 
# 
# # Draw and fill the front of the house
# t.penup()
# t.goto(-150, -120)
# t.pendown()
# drawRectangle(t, 100, 110, "maroon")
 
# # Draw and fill the ffrom turtle import * ront door
# t.penup()
# t.goto(-120, -120)
# t.pendown()
# drawRectangle(t, 40, 60, "black")
 
# # Front roof
# t.penup()
# t.goto(-150, -10)
# t.pendown()
# drawTriangle(t, 100, "linen")
 
# # Side of the house
# t.penup()
# t.goto(-50, -120)
# t.pendown()
# drawParallelogram(t, 60, 110, "mint cream")
 
# # Window
# t.penup()
# t.goto(-30, -60)
# t.pendown()
# drawParallelogram(t, 20, 30, "black")
 
# # Side roof
# t.penup()
# t.goto(-50, -10)
# t.pendown()
# t.fillcolor("old lace")
# t.begin_fill()
# t.left(30)
# t.forward(60)
# t.left(105)
# t.forward(100 / math.sqrt(2))
# t.left(75)
# t.forward(60)
# t.left(105)
# t.forward(100 / math.sqrt(2))
# t.left(45)
# t.end_fill()
# done()

# from turtle import * 
# import colorsys as cs
# hideturtle()
# speed("fastest")
# bgcolor("black")
# width(2)
# h = 0.0
# for i in range(50):
#     col = bgcolor.hsv_to_rgb(h,1,2)
#     color(col)
#     for j in range(10):
#         circle(i*2)
#         right(36)
#     h += 0.1
# done()
    
