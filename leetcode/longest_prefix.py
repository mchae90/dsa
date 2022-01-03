def longestCommonPrefix(strs):
    res = ''
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or strs[0][i] != s[i]:
                return res
            print(i, s, strs[0][i])
        res += strs[0][i]
    return res

longestCommonPrefix(["flower","flow","flight"])