from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for n in nums:
            key = n
            res[key]+=1
        return sorted(res.keys(), key=lambda num:res[num], reverse=True)[:k]