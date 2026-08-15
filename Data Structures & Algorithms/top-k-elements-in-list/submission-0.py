class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        for num in nums:
            if num not in mapp:
                mapp[num] = 1
            else:
                mapp[num] += 1
        result = []
        for i in range(k):
            max_num = max(mapp,key=mapp.get)
            result.append(max_num)
            del mapp[max_num]
        return result

        