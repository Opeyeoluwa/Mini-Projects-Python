def validPalindrome(self, s: str):
    def firstcheck(i,j, removed=False):
        while i<j:
            if s[i]!=s[j]:
                if removed:
                    return False
                return firstcheck(i+1, j, True) or firstcheck(i, j-1, True)

            i +=1
            j -=1
        return True
    return firstcheck(0,len(s)-1)