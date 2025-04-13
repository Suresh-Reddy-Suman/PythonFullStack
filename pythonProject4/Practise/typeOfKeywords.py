# Create a method to accept unlimited args and add them
def add(*args):
    print(type(args))
    total = 0
    for value in args:
        total += value
    print(total)

add(1,2,4,5,6,7)

# Create a Keyword arguments with a function

def employee_details(**kwargs):
    print(kwargs.get('Name', "Venkata"))
    print(kwargs['Age'])
    print(kwargs['Email'])


employee_details(Name='Suresh',Age=24, Email='bagisuresh411@gmail.com')
