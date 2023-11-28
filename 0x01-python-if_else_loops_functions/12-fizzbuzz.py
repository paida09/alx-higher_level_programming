#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz ", end="")
        elif num % 5 == 0:
            print("Buzz ", end="")
        elif num % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{num} ", end="")
    nb = 0
    # multiply a exactly b times
    if b < 0:
        nb = b
        b = (-1) * b

    for i in range(b):
        result *= a
        base = result * result

    if nb < 0:
        result /= base
    return result
