class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Binary Search 방식으로 해결해야 함
        left = 0
        right = len(nums) -1
        
        while(left <= right) :
            center = (left + right) // 2
            
            if(nums[center] > target) :     # 좌측 탐색
                right = center - 1
            elif(nums[center] < target) :   # 우측 탐색
                left = center + 1
            else :
                return center
        
        return left