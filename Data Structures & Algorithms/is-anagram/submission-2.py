class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_sorted_string(s: str) -> str:
            l = list(s)
            l.sort()
            return ''.join(l)
        return get_sorted_string(s) == get_sorted_string(t)