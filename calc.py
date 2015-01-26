import math as m
import time as t
print "\nWelcome to the indirect Object Height Calculator!"
print "---created by JP\n"

k = input("Please enter your eye-height in inches (just the number, please): ")
theta = input("Enter the hypsometer reading: ")
print """What measurement did you use to measure the distance from your eye to the object?
1. inches
2. feet
"""
measurement = input("> ")
if measurement == 1:
    x = input("Enter the distance from your eye to the object in inches: ")
elif measurement == 2:
    feet = input("Enter the distance from your eye to the object in feet: ")
    x = feet * 12
print "Calculating Trig..."
t.sleep(1)
#y = x * m.tan(m.radians(theta))
#height = y + k

height = ( x * m.tan(m.radians(theta)) ) + k

print ("The building's height is"), 
print height,
print "inches"
