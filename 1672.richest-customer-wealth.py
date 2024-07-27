class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > richest:
                richest = sum(accounts[i])
        return richest