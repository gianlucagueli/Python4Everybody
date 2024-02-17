count = 0
tot = 0

while True:
    sval = input('Enter a value:')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    tot = tot + fval 
    count = count + 1

if(count > 0): 
    print(tot, count, tot/count)
else:
    print(tot, count, 0)