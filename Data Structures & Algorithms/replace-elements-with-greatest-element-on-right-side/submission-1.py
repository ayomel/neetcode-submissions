class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        for index in range(len(arr)-1, -1 ,-1):
            newMax = max(max_right, arr[index])
            arr[index] = max_right
            max_right = newMax
        return arr
