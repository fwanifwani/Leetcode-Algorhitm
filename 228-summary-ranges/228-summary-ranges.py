class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start_index=0

        for i in range(len(nums)):
            if i + 1 >=len(nums) or nums[i+1]-nums[i] != 1:
                s = str(nums[start_index])
                e =  str(nums[i])
                result.append(s + "->" + e if s != e else s)
                start_index =i+1

        return result
