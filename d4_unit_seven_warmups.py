my_name = "Brian"
new_letter = ""


for letter in my_name:
    if letter == "i":
        new_letter = new_letter + "y"
    else:
        new_letter = new_letter + letter


print(new_letter)