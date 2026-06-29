class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:
        memo=[[-1 for _ in range(n)] for _ in range(m)]
        def f(n,m):
            if n==0 and m==0:
                return 1
            if n<0 or m<0:
                return 0
            if memo[n][m]!=-1:
                return memo[n][m]
            memo[n][m]=f(n-1,m)+f(n,m-1)
            return memo[n][m]

        return f(m-1,n-1)

