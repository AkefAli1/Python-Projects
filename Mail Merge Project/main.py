PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    list_of_names = names.readlines()
    print(list_of_names)

with open("./Input/Letters/starting_letter.txt") as stl:
    contents = stl.read()


for name in list_of_names:
    stripped_name = name.strip()
    new_letter = contents.replace(PLACEHOLDER, stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as final:
        final.write(new_letter)



