class Solution:
    # TC -> O(n^2) SC -> O(N) which is used by Tim Sort
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        store = set()
        nums.sort() 
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j <= k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == 0:
                    if i!=j and i!=k and j!= k:
                        store.add(tuple((nums[i], nums[j], nums[k])))
                if curSum > 0:
                    k -= 1
                else:
                    j += 1
        return list(store)
                