#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# My code
last=number[-1]
if last>5:
    print("Last digit of",number,"is",last,"and is greater than 5")
elif last ==0:
    print("Last digit of",number,"is",last,"and is greater than 0")
elif last<6 && last!=0:
    print("Last digit of",number,"is",last,"and is less than 6 and not 0")