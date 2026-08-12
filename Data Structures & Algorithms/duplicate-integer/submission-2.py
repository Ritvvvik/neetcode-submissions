class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = {}
        for num in nums:
            if num not in mapp:
                mapp[num] = 1
            else:
                mapp[num] += 1
        
        for num in mapp:
            if mapp[num] > 1:
                return True
        return False



        

        