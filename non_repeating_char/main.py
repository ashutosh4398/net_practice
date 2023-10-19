def firstNonRepeatingCharacter(string):
    # Write your code here.
    visited = {}
    for char in string:
        visited[char] = visited.get(char, 0) + 1
    
    for idx, char in enumerate(string):
        if visited[char] == 1:
            return idx
            
    return -1