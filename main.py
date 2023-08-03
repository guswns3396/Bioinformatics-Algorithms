import sys
from scripts import runScript

if __name__ == '__main__':
    with open(sys.argv[3]) as f:
        args = f.read().splitlines()
    with open('answer.txt', 'w') as f:
        res = runScript(sys.argv[1], sys.argv[2], *args)
        print(res)
        if hasattr(res, '__iter__') and not isinstance(res, str):
            f.write(' '.join([str(x) for x in res]))
        else:
            f.write(str(res))
