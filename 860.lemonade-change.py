class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        change = {'5': 0, '10': 0}
        for b in bills:
            if b == 5:
                change['5'] += 1
            elif b == 10:
                if change['5'] < 1:
                    return False
                else:
                    change['5'] -= 1
                    change['10'] += 1
            else:
                if change['5'] < 1:
                    return False
                if change['10'] < 1:
                    if change['5'] < 3:
                        return False
                    else:
                        change['5'] -= 3
                else:
                    change['10'] -= 1
                    change['5'] -= 1
        return True
        