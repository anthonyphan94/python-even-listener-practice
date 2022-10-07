import turtle
from turtle import *

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def turn_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    tim.speed('fastest')
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

def turn_right_while_run():
    tim.forward(10)
    tim.right(5)
def turn_left_while_run():
    tim.forward(10)
    tim.left(5)



screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward,key='s')
screen.onkey(fun=turn_clockwise, key='d')
screen.onkey(fun=turn_counter_clockwise,key='a')
screen.onkey(fun=clear_screen, key='space')

screen.onkey(fun=turn_right_while_run, key='e')
screen.onkey(fun=turn_left_while_run, key='q')



screen.exitonclick()