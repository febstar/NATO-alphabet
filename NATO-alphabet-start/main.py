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

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
empty = []


db = pandas.read_csv("nato_phonetic_alphabet.csv")
db_dict = pandas.DataFrame(db.to_dict())



nato_dict = {row.letter:row.code for (index, row) in db.iterrows()}
print(nato_dict)
data = input("what is your name?").upper()

# for (index, row) in db_dict.iterrows():
#     for i in data:
#         if row.letter == i:
#             empty.append(row.code)
output_list = [nato_dict[letter] for letter in data]
print(output_list)
