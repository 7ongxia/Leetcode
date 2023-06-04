class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        response = 0
        substring_hash = set()
        i_s = 0
        i_e = 0

        while i_e < len(s):
            if s[i_e] not in substring_hash:
                substring_hash.add(s[i_e])
                response = max(len(substring_hash), response)
                i_e += 1
            else:
                substring_hash.discard(s[i_s])
                i_s += 1

        return response
