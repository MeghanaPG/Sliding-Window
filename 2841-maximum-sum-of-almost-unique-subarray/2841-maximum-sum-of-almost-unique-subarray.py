class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        from collections import defaultdict
        n = len(nums)
        l = 0 
        r = 0 
        num_sum = 0 
        res = 0 
        freq = defaultdict(int)
        unique_count = 0

        while r < n:
            if freq[nums[r]] == 0:
                unique_count += 1
            freq[nums[r]] += 1 
            num_sum += nums[r]
            r += 1

            # shrink the window from the left
            while r - l > k:
                freq[nums[l]] -= 1 
                if freq[nums[l]] == 0:
                    unique_count -= 1 
                num_sum -= nums[l]
                l += 1

            if r - l == k and unique_count >= m:
                res = max(res, num_sum)
        return res 
        
