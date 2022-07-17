import math

tolerance = 0.000001


def newton(n, estimate):
    # Initialize the estimate
    # estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + n / estimate) / 2
        difference = abs(n - estimate ** 2)
        if difference <= tolerance:
            return estimate
        else:
            # if it doesn't match, recursively call the method # newton with input x and updated estimate value
            return newton(n, estimate)


# main method - start point

def main():
    # loop until user presses enter
    while True:
        number = input("Enter a positive number or press Enter to exit: ")
        if number == "":  # 'enter' is pressed. terminate program
            break
        if len(number) > 0:
            estimate = newton(int(number),  1.0)
        else:
            print("You must enter an integer number")
            break

        print("The program's estimate is ", estimate)
        print("Python's estimate is ", math.sqrt(int(number)))


if __name__ == "__main__":
    main()
