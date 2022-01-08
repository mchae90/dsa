def compress_string(s):
    result = ''
    for i, c in enumerate(s):
        cur_char = c
        count = 1
        if i < len(s):
            print(i, len(s))
            if s[i + 1] == cur_char:
                count += 1
            else:
                result.join(cur_char + str(count))
                count = 1
        # result.join('1')
        # print('result', result)
    return s if result == s else result
    
        
print(compress_string('abccd'))