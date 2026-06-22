# state= 
# f(i) min cost till step i

# basecases:

#     i==0:
#     return cost[i]

#     i==1:
#     return cost[i]

# reccurance relation:
# f(i)=min(f(i-1)+cost[i],f(i-2)+cost[i])
# answer :
# return min(f(i-1),f(i-2))




class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def f(i):
            if i==0:
                return 0
            if i==1:
                return 0
            if i in memo:
                return memo[i]

            memo[i]= min(f(i-1)+cost[i-1],f(i-2)+cost[i-2])
            return memo[i]

        
        return f(len(cost))










        