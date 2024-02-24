class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using extra space  TC -> O(N) SC -> O(N)
        seen = set() 
        for num in nums:
            if num not in seen:
                seen.add(num)
        
        return True if len(seen) != len(nums) else False 

        # Without Using extra space  TC -> O(NlogN) SC -> O(1)
        nums.sort() 
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True 
        return False 