
from typing import List

class Solution:
    def twoNumberSum(self, array: List, targetSum: int):
        # data-structure for quick lookup
        hashmap: dict[int, int] = {x: 1 for x in array}
        for i in array:
            otherHalf:int = targetSum - i
            if hashmap.get(otherHalf) and otherHalf != i:
                return [i, otherHalf]
        
        return []


class TestCases:
    test_cases = [
        ([3, 5, -4, 8, 11, 1, -1, 6], 10, [-1, 11])
    ]
    def __init__(self) -> None:
        self.soln = Solution()
    
    def test(self):
        for index, i in enumerate(self.test_cases):
            resp = self.soln.twoNumberSum(i[0], i[1])
            assert all([x in resp for x in i[2]]), f"Failed Test Case {index}"


TestCases().test()