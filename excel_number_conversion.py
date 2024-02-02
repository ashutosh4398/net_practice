class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle.lower()
        alpha_map = {chr(c): (c - 97 + 1) for c in range(97, 97 + 26)}
        default = 0
        # calculate all the possibilites that can come before n-1
        # eg if my column name is of len 3, then before reaching len 3
        # I would have encountered, len=1 ie 26 and len=2 ie 26*26
        # this below loop handles that part
        for i in range(1,len(columnTitle)):
            default += 26 ** i
        
        # once we have handled, possiblities till n-1 len, then we just have to
        # take care of current length
        for idx, char in enumerate(columnTitle[::-1]):
            offset = alpha_map[char]
            if idx == 0:
                default += offset
                continue
            default += (offset - 1) * (26 ** idx)
        
        return default

s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("zy"))

