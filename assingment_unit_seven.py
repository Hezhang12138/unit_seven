characters = "abcdefghijklmnopqrstuvwxyz"


def main():
    x = int(input("what number do you want to put in?"))
    characters1 = characters[0:x]
    characters2 = characters[x:]
    characters3 = characters2 + characters1
    a = input("which function do you want to proceed? Put in 'e' for encode, 'd' for decode, 'q' for quit")
    if a is "e":
        encode_word = input("what word you want to encode?")
        new_string = ""
        for character in encode_word:
            code = characters.index(character)
            new_character = characters3[code]
            new_string = new_string + new_character
        print(new_string)
    elif a is "d":
        decode_word = input("what word yo want to decode?")
        new_string = ""
        for character in decode_word:
            code = characters3.index(character)
            new_character = characters[code]
            new_string = new_string + new_character
        print(new_string)
    else:
        print("thank you for using!")


main()

