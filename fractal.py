from turtle import Turtle

import math

import sys


def drawKochFractal(width, height, size, level):
    t = Turtle()

    t.hideturtle()

    t.up()

    t.goto(-width // 3, height // 4)

    t.down()

    drawFractalLine(t, size, 0, level);

    drawFractalLine(t, size, -120, level)

    drawFractalLine(t, size, 120, level)


def drawFractalLine(t, distance, angle, level):
    """Either draws a single line in a given direction
    or four fractal lines in new directions."""

    if level == 0:

        drawEquilateralTriangle(t, distance, angle)

    else:

        drawFractalLine(t, distance // 3, angle, level - 1)

        drawFractalLine(t, distance // 3, angle + 60, level - 1)

        drawFractalLine(t, distance // 3, angle - 60, level - 1)

        drawFractalLine(t, distance // 3, angle, level - 1)


def drawEquilateralTriangle(t, distance, angle):
    """Moves the given distance in the given direction."""

    t.setheading(angle)
    t.forward(distance)


def main():
    level = 4
    drawKochFractal(200, 200, 150, level)


main()
