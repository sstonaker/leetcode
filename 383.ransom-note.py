class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = list(magazine)
        for s in ransomNote:
            if s in mag_list:
                mag_list.remove(s)
            else:
                return False
        return True