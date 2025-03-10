ARTHAMETIC_OPERATIONS = ['+', '-', '*', '/']


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


end_of_game = False
arthametic = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = int(input("What's the first number? : "))

while not end_of_game:
    for key in arthametic:
        print(key)
    operation = input('Pick an Operation: ')
    second_number = int(input("What's the second number? : "))

    get_data = arthametic[operation]
    total = get_data(first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {total}")

    do_you_want = input(f"Type 'y' to continue calculating with {total}, or type 'n' to cancel")
    if do_you_want == 'y':
        first_number = total
    else:
        end_of_game = True
