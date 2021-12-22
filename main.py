import pandas
# student_dict = {
#     "student": ["Dhvip", "Kenil", "Heril"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
df_nato_alphabet = pandas.DataFrame(nato_alphabet)
dir_nato_alphabet = {row.letter: row.code for (index, row) in df_nato_alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def phonetic_word():
    word = input("Write Your Word\n>> ").upper()
    try:
        phonetic_lis = [dir_nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry only letter in Alphabet")
        phonetic_word()
    else:
        print(phonetic_lis)


phonetic_word()
