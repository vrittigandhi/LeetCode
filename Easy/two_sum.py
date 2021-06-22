class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        temp = nums.copy()
        nums.sort()
        i = 0
        j = n-1
        result = nums[i] + nums[j]
        while result != target and i < j:
            if result > target:
                j -= 1
            else:
                i += 1
            result = nums[i] + nums[j]
        if nums[j] != nums[i]:
            i = temp.index(nums[i])
            j = temp.index(nums[j])
        else:
            x = nums[i]
            i = temp.index(nums[i])
            temp.remove(x)
            j = temp.index(nums[j]) + 1
        return [i, j]
