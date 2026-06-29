class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        memo={}
        def f(n):
            if n==0:
                return nums[0]
            if n<1:
                return 0
            

            if n in memo:
                return memo[n]
            memo[n]=max(f(n-1),f(n-2)+nums[n])
            return memo[n]
        return f(n-1)
        