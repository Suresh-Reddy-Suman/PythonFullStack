# FileNotFound
try:
    with open('file.txt') as file:
        file.read()
except FileNotFoundError as error_message:
    print(error_message)

# Writing JSON data to file
