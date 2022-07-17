# a = 64
# #this will print a in binary
# bnr = bin(a).replace('0b','')
# x = bnr[::-1] #this reverses an array
# while len(x) < 8:
#     x += '0'
#     bnr = x[::-1]
# print(bnr)

decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        print(decimal, decimal // 2)
        bitString = str(remainder) + bitString

print("%5d%8d%12s" % (decimal, remainder, bitString))
print("The binary representation is", bitString)