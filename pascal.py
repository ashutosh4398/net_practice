from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        # if numRows == 2:
        #     return [[1],[1,1]]
        
        prev_triangle = self.generate(numRows-1)
        prev_row = prev_triangle[-1]
        temp = [1] + [sum([prev_row[i-1], prev_row[i]]) for i in range(1,len(prev_row))] + [1]
        prev_triangle.append(temp)
        return prev_triangle


s = Solution()
x = s.generate(5)
print(x)