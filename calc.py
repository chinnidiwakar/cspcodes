#!/usr/bin/env python
import mathfunc
a=int(input("Please enter first value: "))
b=int(input("Please enter second value: "))
c=input("Please Enter the Operation(+,-,*,/): ")
if c=='+':
    print(a,"+",b,"=",mathfunc.add(a,b))
elif c=='-':
    print(a,"-",b,"=",mathfunc.sub(a,b))
elif c=='*':
    print(a,"*",b,"=",mathfunc.mul(a,b))
elif c=='/':
    print(a,"/",b,"=",mathfunc.div(a,b))
else:
    print("Wrong Operation")
