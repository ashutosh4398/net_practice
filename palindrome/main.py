# "abcd" => ptr = 0,1 => [3,2]
# abcde => ptr = 0,1,2 => [4, 3, 2] => 5/2 => 2.5

def isPalindrome(string):
    # Write your code here.
    n = len(string)
    mid = round(n/2.0)
    for i in range(mid):
        if string[i] != string[n-( i+ 1)]:
            return False
    return True
    