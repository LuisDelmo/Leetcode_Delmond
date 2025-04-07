class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        sEncoded = ''

        for charI in range(len(s)):
            asciiVal = ord(s[charI])
            if not 48 <= asciiVal <= 57:
                if not 97 <= asciiVal <= 122:
                    continue
            sEncoded += s[charI]
            
        return sEncoded == sEncoded[::-1]



# 48 <= asciiVal <= 57

solution = Solution()

txt = "race a car"

retorno = solution.isPalindrome(txt)

print(retorno)

