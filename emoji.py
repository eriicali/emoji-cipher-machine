import random


def create_emoji_list(filename) -> list:
    with open(filename, "r") as file:
        listOfEmojis = file.readlines()
        listOfEmojis = [item.strip() for item in listOfEmojis]
    random.shuffle(listOfEmojis)
    return listOfEmojis


def create_character_list() -> list:
    listOfCharacters = []
    for i in range(97, 123):
        listOfCharacters.append(chr(i))
    for i in range(65, 91):
        listOfCharacters.append(chr(i))
    for j in range(0, 10):
        listOfCharacters.append(str(j))
    listOfCharacters.append(" ")
    return listOfCharacters


def create_dictionaries(listOfEmojis, listOfCharacters) -> tuple:
    emoji_dict_encode = {}
    emoji_dict_decode = {}
    for k in range(len(listOfCharacters)):
        emoji_dict_encode[listOfCharacters[k]] = listOfEmojis[k]
        emoji_dict_decode[listOfEmojis[k]] = listOfCharacters[k]
    emoji_dict_encode[""] = ""
    emoji_dict_decode[""] = ""
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
    listOfCharacters = create_character_list()
    emoji_dict_encode, emoji_dict_decode = create_dictionaries(listOfEmojis, listOfCharacters)
    print("\n\n\n************** Emoji Cipher Machine ********************")
    print("\n\n\nThis supports any uppercase or lowercase letter, any digit 0-9, and spaces.")
    while True:
        choice = input("\nWould you like to encode or decode? (e/d), anything else will stop the program: ")
        if choice == "e":
            msg = input("Enter your message to encode: ")
            print("Encoded message: " + encode(msg.strip(), emoji_dict_encode))
        elif choice == "d":
            msg = input("Enter your message to decode: ")
            print("Decoded message: " + decode(msg.strip(), emoji_dict_decode))
        else:
            break


if __name__ == "__main__":
    main()