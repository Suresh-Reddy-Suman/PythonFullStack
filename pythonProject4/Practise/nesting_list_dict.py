cities_visited = {
    "Country": "India",
    "cities": ['Hyderabad', 'Nagpur', 'Bangalore'],
    "Time_of_visits": {
        'Hyderabad': 'Winter',
        'Nagpur': 'Rainy',
        'Bangalore': 'Summer'
    }
}

print(cities_visited["cities"][0])
print(cities_visited["Time_of_visits"]['Nagpur'])

travel_log = {
    "France": {
        "cities_visited": ["Paris", "lille", "Dijon"],
        "total_visited": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgarh"],
        "total_visited": 50
    }
}

print(travel_log["Germany"]["cities_visited"][2])