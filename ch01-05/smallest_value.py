smallest = None
for i in [56,4,97,3,11,468,1,64,48,6,64,564,1,54,626,4]:
    if smallest is None:
        smallest = i
    elif smallest > i:
        smallest = i

print("smallest is:", smallest)