class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        res = []
        # for n in nums:
        #     if n in count:
        #         count[n] += 1
        #     else:
        #         count[n] = 1

        # for k, v in count.items():
        #     if v > (len(nums) // 3):
        #         res.append(k)

        # return res

        for n in nums:
            count[n] += 1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            count = new_count
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res
