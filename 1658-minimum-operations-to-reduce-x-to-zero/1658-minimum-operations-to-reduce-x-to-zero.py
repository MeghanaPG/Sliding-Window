class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Time Complexity: O(n)
        # Sliding Window 
        target = sum(nums) - x
        cur_Sum = 0 
        max_window = -1
        l = 0 

        for r in range(len(nums)):
            cur_Sum += nums[r]

            while l<=r and cur_Sum > target:
                cur_Sum -= nums[l]
                l += 1 

            if cur_Sum == target:
                max_window = max(max_window, r - l + 1)

        return -1 if max_window == -1 else len(nums) - max_window