"""
You have a keyboard which has 40 keys - 

4 rows and 10 columns


The rows are as follows - 

1st row - 1 to 0 

2nd row - q to p

3rd row - a to ;

4th row - z to /


You can apply three “transformations” to a keyboard where the keys are exchanged in the following manner - 


Horizontal Transform (H) - This flips the keyboard on a vertical axis. i.e. the axis is between 5th and 6th columns and all the keys on the left are interchanged with the right. 

Example - In the first row - 1 is exchanged with 0, 2 is exchanged with 9, 3 is exchanged with 8 … and so on.


Vertical Transform (V) - This flips the keyboard on a horizontal axis. ie. the axis between the 2nd and the 3rd row. All the keys on the top most row are exchanged with the bottom. 

Example - In the first row - 1 is exchanged with z, 2 is exchanged with x … and so on

In the second row - q is exchanged with a, w is exchanged with s … and so on


Shift - Its an integer. This shifts the keys on the keyboard by that many spots. 

So for a Shift of 2, the keys are moved to the right by 2 spots. So q moves to e, w moves to r … and so on. 


For negative values of integer, the keys shift to the left. When a key is at the end of the row, it just moves onto the next row for the positive shift. It moves to the previous row for negative shift.


Note that shift transform works across rows and not just within the row itself. For eg. Shifting the keyboard by 1 will result in 0 moving to q, p moving to a and so on


You can chain these transforms, that is, you can have a horizontal transform, shift and a vertical transform chained together denoted as H, 2, V


Your program has two inputs - 

1. A string containing the list of transforms like “H,V,-5,H,2,V,V,H”

2. A large amount of text like “asdfgrerwfasdf12333resdf”


The program takes 2) and applies transforms to each character in that string as specified in 1) and outputs the resulting string.

Example - 

1) H,V

2) qw


Output of program will be - ;l 


If your program encounters strings not on your “keyboard” (like “]”) you can just pass it through untransformed to output.


Key points to remember - 

Write clean and readable code

Assume that you are processing a huge text file which you are applying to transform. Like a 1GB big file. So design your logic putting that into consideration.

You can use any language to implement the program.

It is not necessary that the program take the input from a file or command line arguments, You can use static string variables which can be changed.

Output can be printed to a file or the console.

"""

import copy
from pprint import pprint

KEYBOARD = [
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
    ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
    ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"],
    ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"],
]


class Transform:
    def __init__(self, keyboard) -> None:
        self.keyboard = keyboard
        self.rows = len(keyboard)
        self.cols = len(keyboard[0])
        self.max_nums = self.rows * self.cols

    def horizontal_transform(self):
        """
        Horizontal Transform (H) - This flips the keyboard on a vertical axis. i.e. the axis is between 5th and 6th columns and all the keys on the left are interchanged with the right.

        Example - In the first row - 1 is exchanged with 0, 2 is exchanged with 9, 3 is exchanged with 8 … and so on.
        """
        vertical_center_idx = self.cols // 2

        for col in self.keyboard:
            for i in range(vertical_center_idx):
                col[i], col[self.cols - i - 1] = col[self.cols - i - 1], col[i]
        return self.keyboard

    def vertical_transform(self):
        """
        Vertical Transform (V) - This flips the keyboard on a horizontal axis. ie. the axis between the 2nd and the 3rd row. All the keys on the top most row are exchanged with the bottom.

        Example - In the first row - 1 is exchanged with z, 2 is exchanged with x … and so on

        In the second row - q is exchanged with a, w is exchanged with s … and so on
        """
        horizontal_center_idx = self.rows // 2
        for i in range(horizontal_center_idx):
            self.keyboard[i], self.keyboard[self.rows - 1 - i] = (
                self.keyboard[self.rows - 1 - i],
                self.keyboard[i],
            )
        return self.keyboard

    def _transform_integer_to_rows_cols(self, num):
        # l = []
        # while num > 0:
        #     l.append(num % 10)
        #     num = num // 10
        # max_len = len(str(self.max_nums))
        # missing = max_len - len(l)
        # if missing:
        #     l.extend([0 for _ in range(missing)])

        # return l[::-1]
        return [num//self.cols, num % self.cols]

    def shift(self, key):
        """
        Shift - Its an integer. This shifts the keys on the keyboard by that many spots.

        So for a Shift of 2, the keys are moved to the right by 2 spots. So q moves to e, w moves to r … and so on.


        For negative values of integer, the keys shift to the left. When a key is at the end of the row, it just moves onto the next row for the positive shift. It moves to the previous row for negative shift.


        Note that shift transform works across rows and not just within the row itself. For eg. Shifting the keyboard by 1 will result in 0 moving to q, p moving to a and so on


        You can chain these transforms, that is, you can have a horizontal transform, shift and a vertical transform chained together denoted as H, 2, V

        """
        keyboard_cpy = copy.deepcopy(self.keyboard)
        for i in range(self.rows):
            for j in range(self.cols):
                num = (i * self.cols + (j + key)) % (self.rows * self.cols)
                _i, _j = self._transform_integer_to_rows_cols(num)
                self.keyboard[_i][_j] = keyboard_cpy[i][j]
        return self.keyboard

    def sol(self, input_str, transform_str):
        transform_map = {
            "H": self.horizontal_transform,
            "V": self.vertical_transform,
        }
        pos = {}
        for i_r, row in enumerate(self.keyboard):
            for i_c, col in enumerate(row):
                if col in input_str:
                    pos[col] = (i_r, i_c)
        transform_str = transform_str.upper().split(",")

        for transform_char in transform_str:
            method = transform_map.get(transform_char)
            if method:
                self.keyboard = method()
            else:
                shift_num = int(transform_char)
                self.keyboard = self.shift(shift_num)

        string = ""
        for char in input_str:
            if char in pos:
                i, j = pos[char][0], pos[char][1]
                string += self.keyboard[i][j]
            else:
                string += char

        return string


t = Transform(KEYBOARD)
# input_string = "asdfgrerwfasdf12333resdf"
# transform_string = "H,V,-5,H,2,V,V,H"
# x = t.sol(input_string, transform_string)
pprint(t.keyboard)
x = t.shift(1)
# horizontal_transform = t.vertical_transform()
pprint(x)
