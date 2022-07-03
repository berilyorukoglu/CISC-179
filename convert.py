#creating the dictionary
look_up={
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15
    }
    #function definition
def repToDecimal(input,base):
    #value is variable to store the final return value
    #it is initialized with 0
    value=0
    #loop to run from the end of the string to beginning i.e. reverse
    for digit in range(len(input)-1,-1,-1):
        #conversion of the value for the digit
        value = value+(look_up[input[digit].upper()]*(base**(len(input)-1-digit)))
    #returning the value to calling function
    return value

#FUNCTION CALLS
print(repToDecimal("10",8))
print(repToDecimal("10",16))
print(repToDecimal("11111010",2))
print(repToDecimal("FA",16))
print(repToDecimal("1a0",16))
print(repToDecimal("101",5))
