from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = (len(numbers)-1) // 2
        print(i)

        while True:

            if numbers[i] + numbers[i + 1] == target:
                return[i + 1, i + 2]
            elif numbers[i] + numbers[i + 1] < target:
                i = (i + len(numbers) - 1 )// 2
            else:
                i -= 1


            

                

case0 = [1,2,4,5,6]
tar0 = 11


case1 = [2,7,11,15]
tar1 = 9

case2 = [2,3,4]
tar2 = 6

case3 = [-1,0]
tar3 = -1


solution = Solution()

retorno = solution.twoSum(case2,tar2)

print(retorno)