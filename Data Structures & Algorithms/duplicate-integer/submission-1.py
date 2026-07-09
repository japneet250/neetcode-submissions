class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(0,len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False

        temp = set(nums)
        if len(temp) != len(nums):
            return True

        else:
            return False
        