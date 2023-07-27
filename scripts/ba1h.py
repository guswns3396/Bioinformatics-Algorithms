from .ba1g import HammingDistance


def ApproxPatMatch(pat, txt, d):
    pos = []
    for i in range(len(txt) - len(pat) + 1):
        ham = HammingDistance(txt[i:i + len(pat)], pat)
        if ham <= int(d):
            pos.append(i)
    return pos
