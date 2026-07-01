class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=""
        def backtrack(op,cl,stack):
            if op==cl==n:
                res.append("".join(stack))
                return 
            if op<n:
                
                backtrack(op+1,cl,stack+"(")
                
            if cl<op:
                
                backtrack(op,cl+1,stack+")")
                
            
        backtrack(0,0,"")
        return res