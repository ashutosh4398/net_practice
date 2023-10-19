# RUN LENGTH ENCODING
# AAA => 3A
# ALL SORTS OF SPECIAL CHARACTERS & NUMBERS
# RUNS GREATER THAN 10 SHOULD BE STORED IN SPLITS
# EG: AAAAAAAAAAAA => 12A => 9A3A
# ABAABAAABBB => 
# [1A, 1b, ]
# A => 1A
# AA => 2A
# AB => 1A1B

def format_score(score, char) -> str:
    return f"{score}{char}"


def runLengthEncoding(string: str) -> str:
    # Write your code here.
    encoded_list: list[str] = []
    cached_score = 0
    n = len(string)
    for i in range(n):
        current_idx, next_idx = i, i+1
        cached_score += 1
        if next_idx <= (n-1) and (string[current_idx] != string[next_idx] or cached_score == 9):
            encoded_list.append(format_score(cached_score, string[current_idx]))
            cached_score = 0
        
    encoded_list.append(format_score(cached_score, string[current_idx]))
    return ''.join(encoded_list)
        

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))