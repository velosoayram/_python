part = []
partY = []
partN = []
amig = []
while True:
    r = str(input()).strip()
    if r == 'FIM':
        break
    r = r.split()
    if r not in part:
        part.append(r)
        if 'YES' in r:
            partY.append(r)
            amig.append(r[0])
        elif 'NO' in r:
            partN.append(r)
partY.sort()
partN.sort()
part = partY + partN
for p in part:
    print(p[0])
amig.sort(key=len, reverse=True)
print('\nAmigo do Habay:')
print(f'{amig[0]}')
