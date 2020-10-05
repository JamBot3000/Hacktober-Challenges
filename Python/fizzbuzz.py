#!/usr/bin/env python3
import sys

def fizzbuzz_naive(number: int):
    """Print Fizzbuzz until a certain number.

    This is a straightforward implementation using if/elif/else syntax."""
    for i in range(1, number+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

def fizzbuzz_hacky(number: int):
    """Print Fizzbuzz until a certain number, using a hacky approach.

    This implementation abuses the carriage return character, using it
    to overwrite "Fizz" and "Buzz" on top of the printed numbers.
    It should not be used in production, but is fun to write and understand!"""
    for i in range(1, number+1):
        print(i, end='\r')
        if i%3 == 0:
            print('Fizz', end='')
        if i%5 == 0:
            print('Buzz', end='')
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: %s <number>" % sys.argv[0], file=sys.stderr)
        sys.exit(1)
    fizzbuzz_hacky(int(sys.argv[1]))
