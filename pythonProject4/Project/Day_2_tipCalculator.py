print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? $ '))
tip_percentage = int(input('How much tip would you like to give? 10, 12, or 15? '))
number_of_people = int(input('How many people to split the bill? '))

tip_amt = (total_bill * tip_percentage) / 100
for_person = round((total_bill + tip_amt) / number_of_people, 2)

print(f'Each person should pay: ${for_person}')
