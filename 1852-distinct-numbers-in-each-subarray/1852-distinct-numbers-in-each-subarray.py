# class Solution:
#     def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
#         # ans[i] is the number of distinct number in the subarray
#         myHash = {i:[] for i in range(len(nums) - k+1)} 
#         res = [0] * (len(nums) - k + 1)
#         # i = 0 => nums[0:2] => nums[i:i+k-1]
#         # i = 1 => nums[1:3]

#         for i in range(len(nums)-k+1):
#             myHash[i] = len(set(nums[i:i+k]))
#         # print(myHash)

#         # from the hashmap values take the number of distinct values and then 
#         # store that in the result 
#         for key, valuelist in myHash.items():
#             res[key] = valuelist
#         return res 

# sliding window and hashmap
from collections import defaultdict

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        # Initialize frequency map and result list
        freq = defaultdict(int)
        res = [0] * (len(nums) - k + 1)
        distinct_count = 0

        # Populate the frequency map for the first window
        for i in range(k):
            if freq[nums[i]] == 0:
                distinct_count += 1
            freq[nums[i]] += 1

        # Store the result for the first window
        res[0] = distinct_count

        # Slide the window over the rest of the array
        for i in range(1, len(nums) - k + 1):
            outgoing = nums[i - 1]
            incoming = nums[i + k - 1]

            # Remove the outgoing element
            if freq[outgoing] == 1:
                distinct_count -= 1
            freq[outgoing] -= 1

            # Add the incoming element
            if freq[incoming] == 0:
                distinct_count += 1
            freq[incoming] += 1

            # Store the distinct count for the current window
            res[i] = distinct_count

        return res
