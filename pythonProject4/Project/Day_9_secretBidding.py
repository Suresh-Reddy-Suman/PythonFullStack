print('Welcome to secret auction program')

complete_bidding = False
bidding_data = {}

while not complete_bidding:

    name = input('What is your name? : \n')
    bid_amt = int(input("What's your bid? : \n"))

    bidding_data[name] = bid_amt
    new_bidder = input('yes or no')
    if new_bidder == 'no':
        final_amt = 0
        for data in bidding_data:
            if bidding_data[data] > final_amt:
                final_amt = bidding_data[data]
            winner = data
        print(f'{winner} with {final_amt} is the winner')
        complete_bidding = True
