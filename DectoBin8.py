a = 64
#this will print a in binary
bnr = bin(a).replace('0b','')
x = bnr[::-1] #this reverses an array
while len(x) < 8:
    x += '0'
    bnr = x[::-1]
print(bnr)