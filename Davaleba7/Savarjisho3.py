

text1 = "Hello"





def reverseString(text):
   if text == "":
    return text
   else:
    return reverseString(text[1:]) + text[0]



print(reverseString(text1))