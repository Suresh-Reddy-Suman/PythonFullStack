from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

TURN_OFF = False
menu = Menu()
coffeemaker = CoffeeMaker()
my_money_machine = MoneyMachine()

while not TURN_OFF:
    choice = input(f'What do you like? {menu.get_items()} : ')

    if choice == 'report':
        coffeemaker.report()
        my_money_machine.report()
    elif choice == 'off':
        TURN_OFF = True
    else:
        menuItem = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(menuItem):
            my_money_machine.make_payment(menuItem.cost)
            coffeemaker.make_coffee(menuItem)
