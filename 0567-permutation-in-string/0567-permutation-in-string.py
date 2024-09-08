class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def sort_string(s:str) -> str:
            return ''.join(sorted(s))

        s1_sorted = sort_string(s1)
        
        # Ensure that the loop checks all valid starting positions for a substring in s2 that has the same length as s1.
        for i in range(len(s2) - len(s1) + 1):
            if s1_sorted == sort_string(s2[i: i+len(s1)]):
                return True
        return False
        