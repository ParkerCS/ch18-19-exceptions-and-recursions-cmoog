'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''

import turtle

def fractal(x, y, distance, index):
    my_turtle = turtle.Turtle()
    if index == 0:
        my_turtle.showturtle()
        my_screen = turtle.Screen()
        my_screen.bgcolor('blue')
        index += 1
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()

    my_turtle.setheading(90)
    my_turtle.forward(distance)

    fractal(my_turtle.xcor(), my_turtle.ycor(), distance/10, index)

fractal(100, 100, 100, 0)

