logo = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
print(logo)

print('Welcome to Treasure Island')
print('You mission is to find the treasure.')
choice_1 = input("You're at a cross road. Where do you want to go?"'\n\t Type "left" or "right"')
if choice_1 == 'left':
    choice_2 = input(
        "You've come to a lake. There is an island in the middle of the lake."
        '\n\t Type "wait" to wait for a boat. Type "swim" to swim across')
    if choice_2 == 'wait':
        choice_3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors."
            "\nOne red, one yellow and one blue. Which color do you choose?")
        if choice_3 == 'yellow':
            print('Congratulations! You won the game')
        elif choice_3 == 'red':
            print('Burned by fire. Game Over!!')
        elif choice_3 == 'blue':
            print('Eaten by beasts. Game Over!!')
        else:
            print('Game Over')
    else:
        print('Attacked by trout. Game Over!!')
else:
    print("Fall into a hole. Game Over!!")
