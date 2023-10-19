from typing import List, Dict

def commonCharacters(strings: List[str]) -> List[str]:
    # Write your code here.
    previousChars = {char: 1 for char in strings[0]}
    for string in strings[1:]:
        currentChars: Dict[str, int] = {char: 1 for char in string}
        keysToPop: List[str] = []
        for character in currentChars:
            if character not in previousChars:
                keysToPop.append(character)
        
        for key in keysToPop:
            currentChars.pop(key)
        previousChars = currentChars
    
    return list(previousChars.keys())


print(commonCharacters(["abc", "bcd", "cbaccd"]))