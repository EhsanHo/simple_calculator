print("*** User Manual ***")
print(' Use + for Addition ')
print(' Use - for Subtraction ')
print(' Use * for Multiplication ')
print(' Use / for Division ')
print(' Use ** for Exponentiation ')
print(' Use /// for Extraction nth root ')
print()

a=float(input("Enter first number:"))
b=input("Enter operator:")
c=float(input("Enter second number:"))

if b=='+':
    e=a+c
    print("The result:",e)

elif b=='-':
    e=a-c
    print("The result:",e)

elif b=='*':
    e=a*c
    print("The result:",e)

elif b=='/':
    e=a/c
    print("The result:",e)

elif b=='**':
    e=a**c
    print("The result:",e)

elif b=='///':
    e=a**(1/c)
    print("The result:",e)

