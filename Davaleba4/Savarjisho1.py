

text = input("Enter word: ").lower()

reversedText = ""

textLength = len(text)


for i in range(textLength):
    letter = text[textLength - 1 - i]
    reversedText = reversedText + letter

print(reversedText)

if text == reversedText:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")

