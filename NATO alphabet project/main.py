

import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(df)
# print(df.letter)

new_dict = {df.letter[index]: df.code[index] for (index, row) in df.iterrows()}
# print(new_dict)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
new_list = [letter.upper() for letter in user_input]
# print(new_list)
new_list1 = [new_dict[item] for item in new_list]
print(new_list1)
