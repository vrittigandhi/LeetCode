class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_2 = nums.copy()            
        for i in nums:
            x = nums_2.count(i)
            for y in range(x-1):
                nums.remove(i)
        return len(nums)
    
    
