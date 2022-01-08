def check_permutation(s1, s2):
    hash_map = {}
    if len(s1) != len(s2):
        return False
    for c in s1:
        if c not in hash_map:
            hash_map[c] = 1
        else:
            hash_map[c] += 1
    for c in s2:
        if c not in hash_map:
            return False
        else:
            hash_map[c] -= 1
    if any (i > 1 for i in hash_map.values()):
        return False
    return True

print(check_permutation('ab;a', 'baa'))