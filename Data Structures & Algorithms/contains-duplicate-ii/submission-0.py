class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mySet = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                mySet.remove(nums[left])
                left += 1

            if nums[right] in mySet:
                return True

            mySet.add(nums[right])

        return False