

winadadeba = "The wind howled and howled all night long"


def count_words(sentece):


    resultDict = {}


    words = sentece.split()

    for i in words:
        if i in resultDict:
            resultDict[i] += 1
        else:
            resultDict[i] = 1


    return resultDict


print(count_words(winadadeba))

