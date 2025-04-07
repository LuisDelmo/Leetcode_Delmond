class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(len(nums)):
            numero = nums[i]
            paratarget = target - numero


            if paratarget in hashmap.keys():
                return [hashmap[paratarget], i]
            
            hashmap[numero] = i
            
            
            
nums1 = [-3,4,3,90]
nums2 = [2,7,11,15]  
solution = Solution()      

retorno = solution.twoSum(nums= nums1, target= 0)
retorno2 = solution.twoSum(nums= nums2, target= 9)

print(retorno)