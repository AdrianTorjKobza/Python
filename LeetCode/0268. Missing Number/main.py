class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_len = len(nums)

        for i in range(nums_len + 1):
            print("i: ", i)
            exist = False
            
            for value in nums:
                print("value: ", value)
                if value == i:
                    exist = True
                    break

            if exist == False:
                result = i
                break

        return result

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

solution = Solution()
missing_number = solution.missingNumber(nums)
print("Missing number: ", missing_number) # Missing number: 8