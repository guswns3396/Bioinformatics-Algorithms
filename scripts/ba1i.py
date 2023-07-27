from .ba1g import HammingDistance


def CountApproxPatMatch(pat: str, txt: str, d: int):
    pos = []
    for i in range(len(txt) - len(pat) + 1):
        ham = int(HammingDistance(txt[i:i + len(pat)], pat))
        if ham <= int(d):
            pos.append(i)
    return len(pos)
