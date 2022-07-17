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


def drawEquilateralTriangle(turtle, distance, angle):
    turtle.setheading(angle)
    turtle.forward(distance)


def main():
    turtle = Turtle()
    level = int(input(" Enter level :"))
    turtle.width = 200
    turtle.height = 200
    turtle.size = 150
    #turtle.hideturtle()


# The entry point for program execution
if __name__ == "__main__":
    main()

