class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in strs:
            
            encoded += str(len(i))
            encoded += "$"
            encoded += i
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!= "$":
                
                j+=1
            k=s[i:j]
            length=int(k)

            wordstrt=j+1
            wrdend=wordstrt+length

            deco=s[wordstrt:wrdend]
            decoded.append(deco)
            i= wrdend

        return decoded
        
