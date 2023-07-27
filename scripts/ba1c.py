def ReverseComplement(txt: str):
    mapping = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    rc = ''
    for i in range(len(txt)):
        rc += mapping[txt[-i - 1]]
    return rc
