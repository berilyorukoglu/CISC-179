def check_user_input(input):
    invalidcharacters = "!@#$%^&*()_+="
    if isinstance(input, int):
        print("You have entered an integer")

    if isinstance(input, float):
        print("You have entered an integer")

    if isinstance(input, str):
        print("You have entered a string")

    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")
            if not input.isalpha():
                print("The value contains non-alphabet characters")
                if any(char in invalidcharacters for char in input):
                    print("Special characters exists in the input")
                else:
                    print("No special characters are present in the string")



x = input("Enter a value of any type: ")
check_user_input(x)
