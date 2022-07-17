def isSorted(alist):
    if len(alist) == 0 or len(alist) == 1:
        return True
    # Loop through and compare each item to the previous item
    count = 0
    for i in range(1, len(alist)):
        if alist[i - 1] < alist[i]:
            count += 1
    if count == len(alist) - 1:
        return True
    else:
        return False


# print(isSorted([1, 2, 3, 5, 6, 4]))
# A main for testing your code
def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))
    lyst = [1, 2, 3, 5, 6, 4]
    print(isSorted(lyst))
    lyst = [0, 2, 3, 5, 6, 7]
    print(isSorted(lyst))


if __name__ == "__main__":
    main()
