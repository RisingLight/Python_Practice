def encodeString(sentence):
    sentence = sentence.split()
    for i in range(len(sentence)):
        sentence[i] = sentence[i].capitalize()
    return "".join(sentence)

def decodeString(sentence):
    if not sentence:
        return ""
    decodedSentence = []
    word = sentence[0]
    for i in range(1,len(sentence)):
        if sentence[i].isupper():
            decodedSentence.append(word)
            word = sentence[i].lower()
        else:
            word += sentence[i]
    decodedSentence.append(word)
    return " ".join(decodedSentence)

sentence = input("Enter a String: ")
encodedSentence = encodeString(sentence)
decodedSentence = decodeString(encodedSentence)
print("Converted String is {}".format(encodedSentence))
print("Original String is {}".format(decodedSentence))