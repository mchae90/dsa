def string_unique_chars(s):
    chars = {}
    for c in s:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    if any (i > 1 for i in chars.values()):
        return False
    return True

print(string_unique_chars('sade]=-0e'))