characters = "abcdefghijklmnopqrstuvwxyz"
encode_word = input("what word you want to encode?")
decode_word = input("what word yo want to decode?")


def main():
    x = int(input("what number do you want to put in?"))
    characters1 = characters[0:x]
    characters2 = characters[x:26]
    characters3 = characters2 + characters1
    print(characters3)
    characters.index(encode_word)


main()