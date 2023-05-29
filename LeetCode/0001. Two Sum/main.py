class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum = 0
        output = []
        len_nums = len(nums)

        for i in range(len_nums - 1):
            for j in range(1, len_nums):
                sum = nums[i] + nums[j]

                if sum == target and i < j:
                    output = [i, j]

        return output

nums = [5, 2, 0, 7, 11, 15]
target  = 9

solution = Solution()
print(solution.twoSum(nums, target)) # [1, 3]