class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        while k > 1:
            heapq._heappop_max(nums)
            k -= 1
        return heapq._heappop_max(nums)

# LinK : https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# Account : Codebase -- untitled session
