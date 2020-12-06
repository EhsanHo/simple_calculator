print("*** User Manual ***")
print(' Use + to Sum ')
print(' Use - to Subtract ')
print(' Use * to Multiply ')
print(' Use / to Divide ')
print(' Use ** to Exponentiate ')
print(' Use /// to Square ')
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

