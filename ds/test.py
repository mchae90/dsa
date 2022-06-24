def finalString(s):
    
    res = []
    
    for c in s:
        if c == '#':
            if res:
                res.pop()
        else:
            res.append(c)
    
    return res

print(finalString("y#f#o##f"))

# "y#fo##f"
# "y#f#o##f"