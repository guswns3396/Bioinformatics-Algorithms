def FindPositions(pat: str, gen: str):
    pos = []
    for i in range(len(gen) - len(pat) + 1):
        if gen[i:i + len(pat)] == pat:
            pos.append(str(i))
    return pos
