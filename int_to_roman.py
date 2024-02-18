def convert_to_roman(num:int) -> str:
    integers = [10, 5, 1]
    chars = ["X", "V", "I"]
    final = ""
    while num:
        for int_rep, char_rep in zip(integers, chars):
            quo = num // int_rep
            if quo > 0:
                final += char_rep * quo
                num = num % int_rep
                break
            
            if num == int_rep - 1:
                final += f"I{char_rep}"
                num = int_rep - 1 - num
                break
    
    return final

# print(convert_to_roman(14))

for i in range(1,31):
    print(i, convert_to_roman(i))