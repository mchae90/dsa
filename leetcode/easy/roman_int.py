def romanToInt(s):
    count = 0
    symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    last_char = ''
    for i in range(len(s)):
        if last_char == 'I':
            if s[i] == 'V':
                count += 3
                continue
            if s[i] == 'X':
                count += 8
                continue
        if last_char == 'X':
            if s[i] == 'L':
                count += 30
                continue
            if s[i] == 'C':
                count += 80
                continue
        if last_char == 'C':
            if s[i] == 'D':
                count += 300
                continue
            if s[i] == 'M':
                count += 800
                continue
        count += symbol[s[i]]
        last_char = s[i]
    return count

print(romanToInt("MCMXCIV"))

def romanToInt(s):
    count = 0
    symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in range(len(s)):
        if i + 1 < len(s) and symbol[s[i]] < symbol[s[i + 1]]:
            count -= symbol[s[i]]
        else:
            count += symbol[s[i]]
    return count