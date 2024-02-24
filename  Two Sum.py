class Solution:
    # TC -> O(N) SC -> O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        ans = []
        for idx, num in enumerate(nums):
            to_find = target - num
            if to_find in mapper:
                ans.append(idx)
                ans.append(mapper[to_find])
            else:
                mapper[num] = idx 
        return ans