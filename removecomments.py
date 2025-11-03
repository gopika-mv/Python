f = False
res = []

try:
    with open('abc1.txt', 'w+') as f:
        n = input('Enter text: ')
        while n:
            f.write(n + '\n')
            n = input('Enter text: ')
        
        f.seek(0)
        p = f.readlines()
        
        for i in p:
            if not i.strip().startswith('#'):
                res.append(i)

    print("\nLines without comments (#):")
    for line in res:
        print(line, end='')

except IOError as e:
    print(e)
