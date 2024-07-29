class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for j in range(len(rating)):
            smaller_left = 0
            bigger_left = 0
            smaller_right = 0
            bigger_right = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    smaller_left += 1
                elif rating[i] > rating[j]:
                    bigger_left += 1

            for k in range(j + 1, len(rating)):
                if rating[k] < rating[j]:
                    smaller_right += 1
                elif rating[k] > rating[j]:
                    bigger_right += 1
            
            res += smaller_left*bigger_right + bigger_left*smaller_right
    

        return res