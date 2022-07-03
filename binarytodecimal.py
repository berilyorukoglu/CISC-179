bitString = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitString) - 1

for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    print(digit, decimal, exponent)
    exponent = exponent - 1
print("The integer value is", decimal)

# 11001 25
# 100000 32
# 11111   31