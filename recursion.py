from showcallstack import showcallstack


def countDownAndUp(number):
    print(number)
    if number == 0:
        # BASE CASE
        print('Reached the base case.')
        return
    else:
        # RECURSIVE CASE
        countDownAndUp(number - 1)
        #showcallstack()
        print(number, 'returning')
        return

    # This is a comment



countDownAndUp(3)

