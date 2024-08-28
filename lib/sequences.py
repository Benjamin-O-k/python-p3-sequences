#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print('[]')
        return
    num1, num2 = 0, 1
    count = 1
    fib_sequence = [num1]
    while count < length:
        count += 1
        num1, num2 = num2, num1 + num2
        fib_sequence.append(num1)
    print(fib_sequence)
