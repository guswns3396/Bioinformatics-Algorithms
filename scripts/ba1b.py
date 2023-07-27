def FrequencyTable(txt: str, k: int):
    counts = {}
    for i in range(len(txt) - k + 1):
        pat = txt[i:i + k]
        if pat not in counts:
            counts[pat] = 1
        else:
            counts[pat] += 1
    return counts


def BetterFrequentWords(txt: str, k: int):
    counts = FrequencyTable(txt, k)
    count_max = max(counts.values())
    pats_max = []
    for pat in counts:
        if counts[pat] == count_max:
            pats_max.append(pat)
    return pats_max


def RunBetterFrequentWords(txt: str, k: str):
    return BetterFrequentWords(txt, int(k))
