class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0 

        # taking the min 4 and max 4 elements and then taking their 
        # difference
        res = float("inf")
        
        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4,nums))

        for i in range(4):
            res = min(res, max_four[i] - min_four[i])

        return res

            

