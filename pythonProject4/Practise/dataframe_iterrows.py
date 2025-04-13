import pandas

#
# student_data = {
#     'Student': ['Venkata', 'Suresh', 'Reddy'],
#     'Score': [97, 45, 84]
# }
#
# student_score_data = pandas.DataFrame(student_data)
#
# for (index,row) in student_score_data.iterrows():
#     print(row)
#

alphabets = pandas.read_csv('../Project/Day_26_NATOALPHABETS/nato_phonetic_alphabet.csv')

alphabets_dit = {row.letter: row.code for (index, row) in alphabets.iterrows()}
final_list = [alphabets_dit[letter] for letter in "ALEKHYA"]
print(alphabets_dit)
print(final_list)
