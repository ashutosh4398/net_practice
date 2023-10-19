def reverse(string):
    return ''.join([string[i] for i in range(len(string)-1, -1, -1)])

def semordnilap(words):
    # Write your code here.
    lookup = {}
    for word in words:
        lookup[word] = lookup.get(word, 0) + 1
    final = []
    for word in words:
        reversed_word = reverse(word)
        lookup[word] -= 1
        if lookup.get(reversed_word):
            final.append([word, reversed_word])
        
    return final
