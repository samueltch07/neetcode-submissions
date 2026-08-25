class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for i in range(len(nums)):
            mydict[nums[i]] = i

        for i in range(len(nums)):
            x = target - nums[i]

            if x in mydict and mydict[x] != i:
                return [i, mydict[x]]

        return []
        