class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0

        for value in details:
            age = value[11:13]
            
            if int(age) > 60:
                count = count + 1
        
        return count

details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]

solution = Solution()
count_senior = solution.countSeniors(details)
print("No. of seniors > 60 years old:", count_senior) # No. of seniors > 60 years old: 2