from showcallstack import showcallstack


def countDownAndUp(number,count):
    print(number)
    if number == 0:
        # BASE CASE
        print('Reached the base case.')
        return
    else:
        # RECURSIVE CASE
        count += 1

        print('* ', count)
        print('call countDownAndUp', number)
        countDownAndUp(number - 1, count)
        # showcallstack()

        print('r', number)
        return



print('first call')
countDownAndUp(3, 0)
print('I am here now ')