#!/usr/bin/env python3

try: #trying to execute somecode
    port=int(input("Please enter a port number: "))
    if port < 65534 and port > 0:
        print("Your port number is",port)
    else:
        print("Your port number is invalid")
#what to do if value error occurs
except ValueError:
    print("It is not a number")
    exit()
#what to do if keyboard interrupt occurts
except KeyboardInterrupt:
    print("\nYou Pressed Control+C, Exiting")
    exit()
#what to do only if no exceptions are triggered
else:
    print("Task Completed Successfully")
#what to do always.
finally:
    print("Thanks for using this script")
