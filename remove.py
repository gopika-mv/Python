inf = False
try:
    n = int(input('Enter line no. : '))  
    with open('abc.txt', 'r+') as inf:   
        lines = inf.readlines()
        lines.pop(n - 1)  
        inf.truncate(0)   
        inf.seek(0)      
        inf.writelines(lines)
except IOError as ie:
    print(ie)
finally:
    if inf:
        inf.close()
