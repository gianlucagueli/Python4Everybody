import re

choice = input("Actual or sample: ")
if choice is "s" :
    choice = "sample_data.txt"
else :
    choice = "actual_data.txt"

try :
    fh = open("/home/gianluca/Projects/PyhtonForEverybody/ch11/" + choice)
except :
    print("ERROR: File not found!")
    exit

total = 0

for line in fh :
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for num in x :
        total = total + int(num)   

print(total)