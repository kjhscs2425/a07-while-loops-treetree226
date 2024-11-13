# Use turtle graphics to make an infinite spiral
import turtle 
x=20
while True:
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(x+5)
    turtle.right(90)
    turtle.forward(x+5)
    turtle.right(90)
    x=x+10
    