"""File: decimaltobinary.py
Converts a decimal integer to a string of bits."""

decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")

bitString = " "
while decimal > 0:
    remainder = decimal % 2
    decimal = decimal // 2
    bitString = str(remainder) + bitString
print("%5d%8d%12s" % (decimal, remainder, bitString))
print( "The binary representation is", bitString)

print('octal operations')

oct = 437
binbin = bin(oct).replace("0b", "")
print(binbin)

#47
#127
#64

