from typing import List
from math import inf


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        resultado = []
        
        for i in range(len(nums)):
            numero = nums[i]

            if numero not in hashmap:
                hashmap[numero] = 1
            else:
                hashmap[numero] += 1

        for i in range(k):
            maximo = -inf
            numero = 0
            for j in hashmap:
                if hashmap[j] > maximo:
                    maximo = hashmap[j]
                    numero = j

            hashmap.pop(numero)
            resultado.append(numero)

        return resultado



solution = Solution()

nums = [1,1,1,2,2,3]


retorno = solution.topKFrequent(nums = nums, k = 2)

print(retorno)