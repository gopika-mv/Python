

inf = False

try:
    inf = open('file.txt', 'r')
    lines = inf.readlines()
    lines.sort(key=len, reverse=True)
    print("Longest line is:\n", lines[0])
except IOError as e:
    print(e)
finally:
    if inf:
        inf.close()
