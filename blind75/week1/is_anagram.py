class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_map = {}
            
        for c in s:
            if c not in hash_map:
                hash_map[c] = 1
            else:
                hash_map[c] += 1
        
        for c in t:
            if c not in hash_map:
                return False
            else:
                hash_map[c] -= 1
            
            if hash_map[c] < 0:
                return False
        
        return True

# Key: Use hashmap to track occurences of each character.
# TC: O(s + t)
# SC: O(1)
# Another way: sort the two strings, compare they are exact same.