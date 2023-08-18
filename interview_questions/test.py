def bold(s, words):
    # build list of booleans to produce final res
    n = len(s)
    flag = [False] * n

    # end = 0
    # for i in range(n):
    #     for word in words:
    #         if s.startswith(word, i):
    #             end = i + len(word)

    #     flag[i] = i < end

    for word in words:
        start = 0
        while start < n:
            index = s.find(word, start)
            if index != -1:
                for j in range(index, index + len(word)):
                    flag[j] = True
            else:
                start = index + len(word)
            print(start)
    
    print(flag)

    res = ''
    # build final res
    for i in range(n):
        if flag[i] and (i == 0 or (i > 0 and not flag[i - 1])):
            res += '<b>'
        
        res += s[i]

        if flag[i] and (i == n - 1 or (i < n - 1 and not flag[i + 1])):
            res += '</b>'

    return res

print(bold("abcxyz123", ["abc","123"]))


# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"

# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
