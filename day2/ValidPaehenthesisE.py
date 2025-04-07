class Solution:
    def isValid(self, s: str) -> bool:
        tam = len(s)
        fHalf = s[:tam // 2]
        sHalf = s[tam // 2:].replace(']','[').replace('}','{').replace(')','(')

        print(fHalf, sHalf[::-1])

        if fHalf == sHalf[::-1]:
            return True
        return False



s = '([])'
solution = Solution()

retorno = solution.isValid(s)

print(retorno)