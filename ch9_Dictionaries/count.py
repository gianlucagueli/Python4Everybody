counts = dict()
counts2 = dict()

names = ['csev', 'cwen', 'mike', 'csev', 'zqian', 'cwen']

for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
    print(counts)

print("\n\nSecond round:\n")

for name in names : 
    counts2[name] = counts2.get(name, 0) + 1
    print(counts2)