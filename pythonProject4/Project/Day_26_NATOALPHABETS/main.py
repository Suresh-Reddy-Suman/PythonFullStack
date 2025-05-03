# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabets = pandas.read_csv('nato_phonetic_alphabet.csv')

alphabets_dit = {row.letter: row.code for (index, row) in alphabets.iterrows()}
final_list = []
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
end_of_game = False
while not end_of_game:
    name = input('Provide the name \n').upper()
    try:
        final_list = [alphabets_dit[letter] for letter in name]
        print(final_list)
        end_of_game=True
    except:
        print('Sorry, Only alphabets is allowed')
