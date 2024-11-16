from turtle import *


#we want to paint a house
shape("turtle")
#step 1 draw a squear
color("purple")
width(7)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
#end of squear
#drawing door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("purple")
left(30)
forward(100)
color("brown")
begin_fill()
left(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
end_fill()
color("purple")
right(90)
forward(50)
right(90)
forward(200)
right(90)
forward(50)
color("brown")
begin_fill()
right(90)
forward(60)
left(90)
forward(50)
left(90)
forward(60)
left(90)
forward(50)
end_fill() 
color("purple")
forward(50)
left(90)
forward(50)




























exitonclick()








