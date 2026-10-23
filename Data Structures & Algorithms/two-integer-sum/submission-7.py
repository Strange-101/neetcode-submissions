class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tb= {}
        for i,n in enumerate(nums):
            n2 = target-n
            if n2 in tb:
                return [tb[n2],i]
            tb[n]=i
