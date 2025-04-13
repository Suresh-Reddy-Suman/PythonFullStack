# with open("weather_data.csv") as weather_data:
#     day_list = weather_data.readlines()
#
# print(day_list)

# TODO : Get temperatures from the csv file and add to a list

# import csv
#
# with open("weather_data.csv") as weather_data:
#     day_wise_data = csv.reader(weather_data)
#     temperatures = []
#     for row in day_wise_data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# TODO : Importing Pandas and working with them
import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
#
# print(data.condition)
# monday = data[data["day"] == 'Monday']
# # TODO : Convert celcius to Farenheit
# monday_temp = monday.temp[0]
# print((monday_temp * 1.8) + 32)

# TODO : Create a Data frame of dictionary with student score and update to csv file

student_score = {
    "Student_Name": ['Suresh', 'Ramya', 'Abhi'],
    "Scores": [97, 98, 99]
}

score = pandas.DataFrame(student_score)
score.to_csv("Scoredata.csv")
