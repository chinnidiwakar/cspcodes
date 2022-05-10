#!/usr/bin/env python3
try:
    port=int(input("Please enter a port number: "))
    if port < 65535 and port > 0:
        print("Your Port Number is",port)
    else:
        print("Your Port Number is Invalid")
except ValueError:
    print("Its not a number")
    exit()
except KeyboardInterrupt:
    print("\nUser closed the program")
    exit()
else:
    print("Task Completed Successfully")
finally:
    print("Thank You For Using")
