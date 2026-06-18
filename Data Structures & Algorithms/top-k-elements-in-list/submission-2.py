class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashed={}
        for i in nums:
            if i not in hashed:
                hashed[i]=1
            else:
                hashed[i]+=1
        L=sorted(hashed,key=hashed.get)
        L=L[::-1]
        return L[:k]
        