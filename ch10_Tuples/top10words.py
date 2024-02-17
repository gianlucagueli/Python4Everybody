fhand = open("input.txt")
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key,value in counts.items() :
    newtup = (value, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)


# replace from line 8 to 16
print(sorted([ (v,k) for k,v in counts.items() ], reverse=True))