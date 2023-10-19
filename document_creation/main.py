def generateDocument(characters, document):
    # Write your code here.
    dictionary = {}
    for i in characters:
        dictionary[i] = dictionary.get(i, 0) + 1
    for char in document:
        count = dictionary.get(char, 0)
        if count < 1:
            return False
        if count >= 1:
            dictionary[char] -= 1
        
    return True


print(generateDocument("aheaolabbhb", "hello"))