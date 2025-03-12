class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Using while loop
        last_el = len(s) -  1

        count = 0
        while True:
            if s[last_el] == " " and count > 0 or last_el < 0:
                return count  
                
            elif s[last_el] != " ":
                count += 1
            last_el -= 1

        # Using built in split
        # splitted_str = s.split()

        # last_word = splitted_str[-1]
        # return len(last_word)