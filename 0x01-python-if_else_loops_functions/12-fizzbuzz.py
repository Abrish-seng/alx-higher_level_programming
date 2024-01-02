#!/usr/bin/python3
def fizzbuzz():
    """Print the numbers from 1 to 100 separated by a space.

    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    accomulator = f''
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            accomulator += "FizzBuzz "
        elif num % 5 == 0:
            accomulator += "Buzz "
        elif num % 3 == 0:
            accomulator += f'Fizz '
        else:
            accomulator += f'{num} '
    print(accomulator, end="")
