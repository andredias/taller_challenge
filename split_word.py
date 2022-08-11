"""
Write a program to divide a string in n equal parts.		
		
Sample Output:		
		
The given string is: abcdefghijklmnopqrstuvwxy		
The string divided into 5 parts and they are:		
		
abcde		
fghij		
klmno		
pqrst		
uvwxy
"""

def split_word(word: str, number: int) -> list[str]:
    incr = len(word) // number
    result = []
    count = 0
    while count < len(word):
        result.append(word[count:(count + incr)])
        count += incr
    return result


print(split_word('abcdefghijklmnopqrstuvwxy', 5))
