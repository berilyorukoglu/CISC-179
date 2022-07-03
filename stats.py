"""A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers. Define these functions, median and mode,
in a module named stats.py. Also include a function named mean, which computes the average of a
set of numbers. Each function should expect a list of numbers as an argument and return a single number.
Each function should return 0 if the list is empty. Include a main function that tests the three statistical functions
using the following list defined in main:"""
import statistics

def mode(lyst):
    if len(lyst) == 0:
        return 0
    return statistics.mode(lyst)

def mean(lyst):
    if len(lyst) == 0:
        return 0
    return statistics.mean(lyst)

def median(lyst):
    if len(lyst) == 0:
        return 0
    return statistics.median(lyst)

def main():
    xmean = mean(lyst)
    xmedian = median(lyst)
    xmode = mode(lyst)
    print("Mode: ", xmode)
    print("Median :", xmedian)
    print("Mean :", xmean)


if __name__ == '__main__':
    lyst = [3, 1, 7, 1, 4, 10]
    result = 0
    main()


"""An example of the program output is shown below:
List: [3, 1, 7, 1, 4, 10]
Mode: 1
Median: 3.5
Mean: 4.33333333333333
"""