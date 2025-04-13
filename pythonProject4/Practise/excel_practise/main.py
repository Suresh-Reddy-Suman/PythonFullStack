import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(data['Primary Fur Color'].count())
grey_color = len(data[data['Primary Fur Color'] == 'Gray'])
Cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
Black = len(data[data['Primary Fur Color'] == 'Black'])


data = {
    "Fur Color": ['Grey', 'Cinnamon', 'Black'],
    "Count": [grey_color, Cinnamon, Black]
}

new_sheet = pandas.DataFrame(data).to_csv("Fur Color Data.csv")
