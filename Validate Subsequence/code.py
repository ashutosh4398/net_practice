from typing import List
def isValidSubsequence(array: List[int], sequence: List[int]) -> bool:
    # Write your code here.
    subsequence_index: int = 0 # index used to traverse subsequence list
    subsequence_length: int = len(sequence)
    for elem in array:
        # avoiding index error and unnecessary computations if sequence is completely
        # traversed
        if subsequence_index >= subsequence_length:
            break
        if elem == sequence[subsequence_index]:
            subsequence_index += 1
    
    return subsequence_index == len(sequence)

TEST_CASES = (
    ([1,2,3,4], [1,3,4], True),
    ([1,2,3,4], [2,4], True),
    ([1,2,3,4], [3,9], False),
    ([1,2,3,4], [2], True)
)

def test_cases():
    for index, case in enumerate(TEST_CASES):
        resp = isValidSubsequence(array=case[0], sequence=case[1])
        assert resp == case[2], f"Failed test case no: {index}"

test_cases()