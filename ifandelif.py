#!/usr/bin/env python3

op=input("Please Choose the Function('+,-,*,/'): ")
var1=int(input("Please Enter Value 1: "))
var2=int(input("Please Enter Value 2: "))
def add(var1,var2):
        return (var1+var2)
def subs(var1,var2):
        return (var1-var2)
def mul(var1,var2):
        return (var1*var2)
def div(var1,var2):
        return (var1/var2)
if op=='+':
        print(var1,"+",var2, "=", add(var1,var2))
elif op=='-':
        print(var1,"-",var2, "=", subs(var1,var2))
elif op=='*':
        print(var1,"*",var2, "=", mul(var1,var2))
elif op=='/':
        print(var1,"/",var2, "=", div(var1,var2))
else:
        print("calc error")
