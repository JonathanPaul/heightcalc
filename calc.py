import math as m
import time as t
print("\nWelcome to the indirect Object Height Calculator!")
print("---created by JP\n")

k = input("Please enter your eye-height in inches (just the number, please): ")
theta = input("Enter the hypsometer reading: ")
print("What measurement did you use to measure the distance from your eye to the object?\n1. inches\n2. feet")

while 1:
    measurement = input("> ")
    measurement = int(measurement)
    if measurement <= 2:
        x = input("Enter the distance from your eye to the object in inches/feet: ")
        x = float(x)
        if measurement == 2:
            x = x * 12 
            break
        break
    else:
     print("enter 1 or 2")
print("let's go kid!\n")
#y = x * m.tan(m.radians(theta))
#height = y + k
theta = float(theta)
k = float(k)
height = ( x * m.tan(m.radians(theta)) ) + k
print("The building's height is: ",height," inches")