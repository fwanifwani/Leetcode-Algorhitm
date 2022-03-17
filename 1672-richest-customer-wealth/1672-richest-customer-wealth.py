class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #
        wealthy_person = 0
        
        for i in accounts:
            total = sum(i)
            wealthy_person = max(wealthy_person, total)
        return wealthy_person