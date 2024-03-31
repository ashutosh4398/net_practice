# dec = 1000 + 500 + 100 + (100-10) +
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_maps = {
            "I": {"val": 1, "subtractions": []},
            "V": {"val": 5, "subtractions": ["I"]},
            "X": {"val": 10, "subtractions": ["I"]},
            "L": {"val": 50, "subtractions": ["X"]},
            "C": {"val": 100, "subtractions": ["X"]},
            "D": {"val": 500, "subtractions": ["C"]},
            "M": {"val": 1000, "subtractions": ["C"]}
        }

        get_decimal_val = lambda x: roman_maps[x]["val"]

        decimal_no = 0
        next_char = None
        i = 0
        while i < (len(s)):
            next_char = s[i+1] if i < len(s)-1 else None
            current_char = s[i]
            subtraction_list_of_next_char = roman_maps[next_char]["subtractions"] if next_char else []
            if current_char in subtraction_list_of_next_char:
                decimal_no += (get_decimal_val(next_char) - get_decimal_val(current_char))
                i += 1
            else:
                decimal_no += get_decimal_val(current_char)
            i+= 1
        return decimal_no

# XIIX => 10+1+9 =>
    
def main():
    s = Solution()
    print(s.romanToInt("MCMXCIV"))

if __name__ == "__main__":
    main()