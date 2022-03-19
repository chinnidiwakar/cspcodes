#!/usr/bin/env python3
from func import *
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = input('Enter +,-,*,/: ')

if str(c)=='+':
    print("The Addition Two Numbers is :",add(a,b))
elif str(c)=='-':
    print("The Substraction Two Numbers is :",sub(a,b))
elif str(c)=='/':
    print("The Division Two Numbers is :",div(a,b))
elif str(c)=='*':
    print("The Multiplication Two Numbers is :",mul(a,b))
else:
    print("You have selected an invalid option, Please Try again")
    exit()
