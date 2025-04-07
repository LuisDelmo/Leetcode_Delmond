# from typing import List
# from collections import defaultdict
# from ast import literal_eval

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if len(strs) == 0:
#             return [[""]]
        
#         hashmap = defaultdict(list)

#         for s in strs:
#             sorted_s = str(sorted(s))
#             hashmap[sorted_s].append(s)

#         result = str(hashmap.values()).replace("dict_values(", "").replace(")","")
#         return result


# solucao = Solution()

# strs1 = ["eat","tea","tan","ate","nat","bat"]

# receba = solucao.groupAnagrams(strs1)

# print(literal_eval(receba))

# 68ms runtime |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\||||||||||\





# 19 ms de runtime coisa boa

from typing import List
from collections import defaultdict
from ast import literal_eval

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        
        hashmap = defaultdict(list)
        resultado = []

        for s in strs:
            sorted_s = str(sorted(s))
            hashmap[sorted_s].append(s)

        for item in hashmap:
            print(item)
            resultado.append(hashmap[item])


        return resultado

solucao = Solution()

strs1 = ["eat","tea","tan","ate","nat","bat"]

receba = solucao.groupAnagrams(strs1)
print(receba)