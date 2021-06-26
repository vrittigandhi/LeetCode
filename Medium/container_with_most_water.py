class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        p1 = 0
        p2 = len(height) - 1
        while p1 < p2:
            l = height[p1]
            r = height[p2]
            if l < r:
                area = (p2 - p1) * l
                print(p1)
                print(height[p1])
                print(l)
                while height[p1] <= l:
                    p1 += 1
            else:
                area = (p2 - p1) * r
                print(p2)
                print(height[p2])
                print(r)
                while height[p2] <= r and p2:
                    p2 -= 1
            if area >  max_area:
                max_area = area
        return max_area
