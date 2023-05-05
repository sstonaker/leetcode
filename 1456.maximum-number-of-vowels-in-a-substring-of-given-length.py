class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        vowels = 0
        l, r = 0, 0
        for i in range(k):
            if s[i] in "aeiou":
                vowels += 1
            r += 1
        max_vowels = max(max_vowels, vowels)
        print(vowels)
        while r < len(s):
            if s[r] in "aeiou":
                vowels += 1
            if s[l] in "aeiou":
                vowels -= 1
            max_vowels = max(max_vowels, vowels)
            l += 1
            r += 1
        return max_vowels
