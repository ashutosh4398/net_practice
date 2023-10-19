# important
# lower case
# non-negative key int
# only alphabets
# ascii of a => 97 | ascii of z => 122

from typing import List
import unittest

def caesarCipherEncryptor(string: str, key: int) -> str:
    # Write your code here.
    modified_chrs : List[str] = []
    start, end = 97, 122
    modulus = end - start + 1
    for char in string:
        ascii = ord(char)        
        modified_ascii = ((ascii + key - start)%modulus) + start
        modified_chrs.append(modified_ascii)
    
    return ''.join([chr(x) for x in modified_chrs])



class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        print("SETTING UP TEST CASE")
        return
    
    def test_key_with_1(self):
        string = "xyz"
        key = 1
        self.assertEqual(caesarCipherEncryptor(string, key), "yza")
    
    def test_key_with_100(self):
        string = "xyz"
        key = 100
        self.assertEqual(caesarCipherEncryptor(string, key), "tuv")
    
    def test_key_with_26(self):
        string = "xyz"
        key = 26
        self.assertEqual(caesarCipherEncryptor(string, key), "xyz")
    



if __name__ == "__main__":
    unittest.main()
