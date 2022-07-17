from turtle import Turtle


def drawFractalLine(turtle, distance, angle, level):
    if level == 0:
        drawEquilateralTriangle(turtle, distance, angle)
        return
    else:
        # change the angles(60) degrees and change level to level-1
        distance = distance / 3.0
        # call drawFractalLine 4 times
        drawFractalLine(turtle, distance, angle, level - 1)
        drawFractalLine(turtle, distance, angle + 60, level - 1)
        drawFractalLine(turtle, distance, angle - 60, level - 1)
        drawFractalLine(turtle, distance, angle, level - 1)
    return


def drawEquilateralTriangle(turtle, distance, angle):
    turtle.setheading(angle)
    turtle.forward(distance)


def main():
    turtle = Turtle()
    turtle.width = 200
    turtle.height = 200
    turtle.size = 200
    level = 2
    turtle.up()
    turtle.goto(-75, 50)
    turtle.down()

    drawFractalLine(turtle, 120, 0, level)
    drawFractalLine(turtle, 120, -120, level)
    drawFractalLine(turtle, 120, 120, level)
    drawFractalLine(turtle, 120, 0, level)
    # hiding turtle after drawing
    turtle.ht()
    # finishing drawing
    turtle.done()


# The entry point for program execution
if __name__ == "__main__":
    main()

