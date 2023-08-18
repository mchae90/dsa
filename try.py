# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"

# Input: 
# s = "aaabbcc"
    #    0000000
    #    1111
    #        e
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"


def bold(s, words):
    # create list of boolean values for index
    flag = [0] * len(s)
    n = len(s)

    end = 0
    for i in range(len(s)):
        for word in words:
            if s.startswith(word, i):
                end = max(end, i + len(word))
        
        flag[i] = i < end

    # build the final string from list
    # [1111100]
    res = ''
    for i in range(len(s)):
        if flag[i] and (i == 0 or (i > 0 and not flag[i - 1])):
            res += '<b>'
        
        res += s[i]

        
        if flag[i] and (i == n - 1 or (i < n - 1 and not flag[i + 1])):
            res += '</b>'

    return res

print(bold("abcxyz123", ["abc","123"]))
print(bold("aaabbcc", ["aaa","aab","bc"]))
