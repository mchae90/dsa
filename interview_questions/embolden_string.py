def embolden(s, words):
    n = len(s)
    flag = [0] * n

    cur_end = 0

    for i in range(n):
        for word in words:
            if s.startswith(word, i):
                cur_end = max(cur_end, i + len(word))

        flag[i] = i < cur_end

    
    res = ''

    for i in range(n):
        if flag[i] and (i == 0 or (i > 0 and not flag[i - 1])):
            res += '<b>'
        
        res += s[i]

        if flag[i] and (i == n - 1 or (i < n - 1 and not flag[i + 1])):
            res += '</b>'
    
    return res

# TC: O(n^2)
# SC: O(n)

print(embolden("abcxyz123", ["abc","123"]))

# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"Input: 

# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"

