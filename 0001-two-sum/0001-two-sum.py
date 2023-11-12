class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        break_check = False
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    break_check = True
                    return [i,j]
                    break
            if break_check:
                break
        