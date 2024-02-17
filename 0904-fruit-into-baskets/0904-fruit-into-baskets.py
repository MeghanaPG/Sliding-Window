class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Time: O(n)
        # fruitType -> in Basket 
        count = collections.defaultdict(int)   
        l, total, res = 0, 0, 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1 

            # As long as we have more than 2 types of fruits,
            # we will start popping from the left of the array 
            while len(count) > 2:
                f = fruits[l]
                count[f] -= 1 
                total -= 1 
                l += 1 

                if not count[f]:
                    count.pop(f)

            res = max(res, total)
        return res 