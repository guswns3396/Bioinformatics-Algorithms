def HammingDistance(p: str, q: str):
    assert len(p) == len(q)
    d = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            d += 1
    return d
