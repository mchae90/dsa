def is_anagram(s, t):
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
    
    return all(val == 0 for val in hash_map.values())

# Key: Use hashmap to track occurences of each character.
# TC: O(s + t)
# SC: O(1)
# Another way: sort the two strings, compare they are exact same.