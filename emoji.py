import random


def create_emoji_list(filename):
    with open(filename, "r") as file:
        listOfEmojis = file.readlines()
        listOfEmojis = [item.strip() for item in listOfEmojis]
    random.shuffle(listOfEmojis)
    return listOfEmojis


def create_dictionaries(listOfEmojis) -> tuple:
    emoji_dict_encode = {}
    emoji_dict_decode = {}
    characters = []
    for i in range(97, 123):
        characters.append(chr(i))
    for j in range(0, 10):
        characters.append(j)
    characters.append(" ")
    for i in range(37):
        emoji_dict_encode[characters[i]] = listOfEmojis[i]
    for i in range(37):
        emoji_dict_decode[listOfEmojis[i]] = characters[i]
    return emoji_dict_encode, emoji_dict_decode


def encode(msgToEncode, emoji_dict_encode) -> str:
    encodedMsg = ""
    for character in msgToEncode:
        encodedMsg += emoji_dict_encode[character]
    return encodedMsg


def decode(msgToDecode, emoji_dict_decode) -> str:
    decodedMsg = ""
    for character in msgToDecode:
        decodedMsg += emoji_dict_decode[character]
    return decodedMsg


def main():
    listOfEmojis = create_emoji_list("emojis.txt")
    emoji_dict_encode, emoji_dict_decode = create_dictionaries(listOfEmojis)

    while True:
        choice = input("Would you like to encode or decode? (e/d), anything else will stop the program: ")
        if choice == "e":
            msg = input("Enter your message to encode: ")
            print(encode(msg, emoji_dict_encode))
        elif choice == "d":
            msg = input("Enter your message to decode: ")
            print(decode(msg, emoji_dict_decode))
        else:
            break


if __name__ == "__main__":
    main()