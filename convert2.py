def decimalToRep(num,base):
    result = ""
    while(num>0):
        rem = num % base
        if rem in range(10):
            result += str(rem)
        else:           #If base 16
            result += chr(65+(rem%10))
        num = num // base
    result = result[::-1]
    if(result == ""):
        return '0'
    return result

def main():
    """Tests the function."""
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))

# The entry point for program execution
if __name__ == "__main__":
    main()
