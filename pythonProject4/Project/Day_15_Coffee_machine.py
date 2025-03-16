types = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.50
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 1.50
    },

    "cappuccino": {
        "ingredients": {
            "water": 50,
            "coffee": 24,
            "milk": 100,
        },
        "price": 3.00
    }
}

ingredients = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

TURN_OFF = False


def report():
    print(f'Water : {ingredients["water"]}ml')
    print(f'Milk : {ingredients["milk"]}ml')
    print(f'Coffee : {ingredients["coffee"]}g')


def calculate_amt(coffee_type):
    print(f"Coffee Price : ${types[coffee_type]['price']}")
    print("Please insert coins")

    quarters = int(input('Number of Quarters:'))
    dimes = int(input('Number of Dimes:'))
    nickels = int(input('Number of Nickels:'))
    pennies = int(input('Number of Pennies:'))

    total_amt = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

    if total_amt > float(types[coffee_type]['price']):
        print(f"Here is your change:{round(total_amt - float(types[coffee_type]['price']), 2)}")
    elif total_amt < float(types[coffee_type]['price']):
        print(f"Not enough amount to buy the coffee")
    elif total_amt == float(types[coffee_type]['price']):
        print(f"Here is your {coffee_type}! Enjoy ")


def check_sufficient_ingredients(coffee_type):
    coffee_qty = types[coffee_type]['ingredients']
    for item in coffee_qty:
        if coffee_qty[item] < ingredients[item]:
            return True
        else:
            return False


def prepare_coffee(coffee_selected):
    coffee_item = types[coffee_selected]['ingredients']
    for item in coffee_item:
        ingredients[item] -= coffee_item[item]

    print(ingredients)
while not TURN_OFF:
    choice = input('What would you like? (espresso/latte/cappuccino) : ')

    if choice == 'report':
        report()
    elif choice == 'off':
        TURN_OFF = True
    else:
        calculate_amt(choice)
        if check_sufficient_ingredients(choice):
            prepare_coffee(choice)
        else:
            print("Not enough items")
