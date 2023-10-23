def solution(queries):
    db = {}
    res = []

    for q in queries:
        k, f = q[1], q[2]
        v = int(q[3]) if len(q) > 3 else None
        
        if q[0] == 'SET_OR_INC':
            if k not in db: 
                db[k] = {f: v}
            else:
                if f not in db[k]:
                    db[k] = {f: v}
                else:
                    db[k][f] += v
            res.append(str(db[k][f]))
        
        if q[0] == 'GET':
            
            if k not in db:
                res.append('')
            else:
                if f not in db[k]:
                    res.append('')
                else: 
                    res.append(str(db[k][f]))

        if q[0] == 'DELETE':
            
            if k not in db:
                res.append('false')
            else:
                if f not in db[k]:
                    res.append('false')
                else:
                    del db[k]
                    res.append('true')   
        
    return res           