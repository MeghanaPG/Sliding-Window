class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n) or O(26.n)
        # hashmap to count the occurances of each character 
        # r-l+1 is the length of the window 
        count = {}
        res = 0

        l = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1 
                l += 1 

            res = max(res, r - l + 1)
        return res 
            

        # If we have the window whose length is less than or equal to k, then it is valid 

