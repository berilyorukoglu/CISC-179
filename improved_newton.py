# is the estimate is close?
def limitReached(x, estimate):
    return abs(x - estimate ** 2) <= 0.000001


# improve approximation
def improveApproximation(x, current_estimate):
    return (current_estimate + x / current_estimate) / 2


#  Keep improving until limit is reached
def newtonSquare(x, estimate=1.0):
    while not limitReached(x, estimate):
        estimate = improveApproximation(x, estimate)
    return estimate


def main():
    while True:
        number = input("Enter a positive number or press Enter to exit: ")
        if number == "":  # 'enter' is pressed. terminate program
            break
        else:
            print("The Program's estimate is", str(newtonSquare(int(number))))
            print("Python's estimate is", str(int(number) ** 0.5))


if __name__ == "__main__":
    main()
