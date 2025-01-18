# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
name = ""
for letter in range(0, 4):
    name += letters[random.randint(0,4)]

print(name)