class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = nums.count(val)
        for i in range(n):
            nums.remove(val)
        return len(nums)
