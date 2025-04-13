# Create a list by adding 1 to each number in the list

numbers = [1, 2, 3, 4, 5]

added_number = [number + 1 for number in numbers]
print(added_number)

# Create a list of each character in the string using list comprehension

name = "Venkata"

characters = [letter for letter in name]
print(characters)

# Create a list by doubling the number in the range

number_range = [number + number for number in range(1, 5)]
print(number_range)

# Create a list comprehension by get a list with only digits divisble by 2

number_value = [number for number in range(1, 25) if number % 2 == 0]
print(number_value)

# Names using conditional list comprehension
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

four_size_names = [name for name in names if len(name) <= 4]
print(four_size_names)

# Get the names with lenght more than 4 and convert them to upper case

more_than_five_chars = [name.upper() for name in names if len(name) > 5]
print(more_than_five_chars)
