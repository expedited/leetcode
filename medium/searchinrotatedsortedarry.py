class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(index, offset):
            return (index + offset) % len(nums)

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        prev = nums[0]
        res = -1000
        for i in range(1, len(nums)):
            elem = nums[i]
            if elem < prev:
                res = i
                break
            prev = elem
        offset = 0
        if res != -1000:
            offset = res

        # 3) binary search
        low, mid, high = 0, 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            modmid = helper(mid, offset)
            curr = nums[modmid]
            if curr == target:
                return modmid
            if curr < target:
                low = mid + 1
            if curr > target:
                high = mid - 1
        return -1

        # I believe this is a binary search, except you just have to do this modulo offset math with each operation
        # 1) find out the rotation offset

        # 2) for each operation, just do the index + offset / length, helper fn
        # 3) binary search with the offset

    # LinK: https://leetcode.com/problems/search-in-rotated-sorted-array/

