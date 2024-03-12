class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #  Time complexity: O(n)
        window = set()
        L = 0 

        for R in range(len(nums)):
            if R - L > k:
                # this means the window is too big and we go ahead and remove the left most one 
                window.remove(nums[L])
                L += 1

            if nums[R] in window:
                return True
            # if the value is not already in the window, we will add it to the window
            window.add(nums[R])
        return False 
    
