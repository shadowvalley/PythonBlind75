class Solution:
    # TC -> O(N) SC -> O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]* len(nums)
        postfix = [0]*len(nums)

        # Calculate prefix 
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Calculate postfix 
        postfix[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        # final calculate 
        for i in range(len(nums)):
            nums[i] = prefix[i]* postfix[i]
        return nums 
