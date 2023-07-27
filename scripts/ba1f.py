def Skew(genome: str):
    skew = [0]
    mapping = {
        'A': 0,
        'T': 0,
        'G': 1,
        'C': -1
    }
    for nucleotide in genome:
        skew.append(skew[-1] + mapping[nucleotide])
    return skew


def MinSkew(genome: str):
    skew = 0
    min = skew
    minind = [0]

    mapping = {
        'A': 0,
        'T': 0,
        'G': 1,
        'C': -1
    }

    for i, nucleotide in enumerate(genome):
        skew += mapping[nucleotide]
        if skew < min:
            min = skew
            minind = [i+1]
        elif skew == min:
            minind.append(i+1)

    return minind