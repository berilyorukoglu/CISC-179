from polygons import *
from turtle import Turtle

def hexagon (t, length): """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left (60)

def radialHexagons(t, n, length):
    """Draws a radial pattern of n hexagons with the given length."""
    for count in range(n):
        hexagon(t, length)
        t.left(360 / n)

def square(t, length): """"Draws a square with the given length."""
    for count in range(4):
        t.forward(length)
        t.left (90)


t = Turtle()
t.pencolor("blue")
t.hideturtle()
square(t, 50) # Embed a square in a hexagon
hexagon(t, 50)
t. clear() # Erase all drawings
radialHexagons (t, 10, 50) # Shown in Figure 7.3