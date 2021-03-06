# LC 58

# def length_of_last_word(s):
#     return len(s.split()[-1])

def length_of_last_word(s):
    i = len(s) - 1
    length = 0

    while s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length