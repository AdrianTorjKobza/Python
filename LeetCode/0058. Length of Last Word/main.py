class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        
        for i in range(len(s) -1, -1, -1):
            if s[i] == ' ':
                if count > 0:
                    return count
            else:
                count = count + 1

        return count

string_input = "   fly me   to   the moon  "

solution = Solution()
word_length = solution.lengthOfLastWord(string_input)
print("Length of the last word:", word_length) # Length of the last word: 4
