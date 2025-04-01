# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

names_for_letter = []
with open("../Day_24_MailMerge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for value in names:
        names_for_letter.append(value.rstrip())

with open("../Day_24_MailMerge/Input/Letters/starting_letter.txt", mode='r') as letter:
    new_data = letter.read()
    for name in names_for_letter:
        with open(f"../Day_24_MailMerge/Output/ReadyToSend/letter_for_{name}", mode='w') as new_file:
            new_letter = new_data.replace("[name]",name)
            new_file.write(new_letter)

print(new_data.replace("[name]","Suresh"))
# with open("../Day_24_MailMerge/Input/Letters/new.txt", mode='w') as new_file:
#     new_file.write(new_letter)
#     print(new_file.read())

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
