class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = Counter(magazine)
        
        for c in ransomNote:
            if c not in mag_map:
                return False
            else:
                mag_map[c] -= 1
            
            if mag_map[c] < 0:
                return False
        
        return True

# TC: O(n)
# SC: O(1)