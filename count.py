inf = False
try:
    inf = open('file1.txt')
    lines = inf.readlines()
    print(lines)
    print('No. of lines : ',len(lines))
except IOError as ie:
    print(ie)
finally:
    if inf: inf.close()
