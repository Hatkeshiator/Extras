def transpose(l):
    # l has n lists, each with m elements
    # we need a list with m lists, each with n elements, all initially 0.
    n = len(l)
    m = len(l[0])
    r = [[0] * n for k in range(m)]
    for i in range(n):
        for k in range(m):
            r[k][i] = l[i][k]
    return r

def flatten(l):
    res = []
    for ele in l:
        if isinstance(ele, list):
            res += flatten(ele)
        else:
            res.append(ele)
    return res