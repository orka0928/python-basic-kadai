﻿import random

var = random.randint (15,30)

if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
elif var % 3 == 0:
    print("Fizz")
elif var % 5 == 0:
    print("Buzz")
else:
    print(var)