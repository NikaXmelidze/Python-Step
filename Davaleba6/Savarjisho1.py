

firstWord=input("Enter word: ")
secondWord = input("Enter word: ")

def isAnagram(word1, word2):
    word1Sorted = sorted(word1)
    word2Sorted = sorted(word2)
    print(word1Sorted)
    print(word2Sorted)
    if word1Sorted == word2Sorted:
        print("The words are anagrams")
    else:
        print("The words are not anagrams")


isAnagram(firstWord, secondWord)