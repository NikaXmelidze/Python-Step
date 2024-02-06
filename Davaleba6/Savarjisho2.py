
enteredText = input("Enter text: ")
enteredCharacter = input("Enter character: ")

def countChararcters(text, character):
    result = 0

    for i in range(len(text)):
        if text[i] == character:
            result += 1
        else:
            pass

    return result



characterAmount = countChararcters(enteredText, enteredCharacter)

print(characterAmount)