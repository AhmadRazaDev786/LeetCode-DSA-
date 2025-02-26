class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for coustomer in accounts:
            wealth = 0
            for bank in coustomer:
                wealth += bank
            max_wealth = max(max_wealth, wealth)
        return max_wealth