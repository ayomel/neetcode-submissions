class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for index, value in enumerate(nums):
            different = target - value
            if different in myMap:
                return [myMap[different], index]
            myMap[value] = index
        return []
 

        