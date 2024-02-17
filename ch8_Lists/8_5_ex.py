# 8.5 Open the file mbox-short.txt and read it line by line. 
# en you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and 
# print out the second word in the line (i.e. the entire address of the person who sent the message). 
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the count.

fname = input("Enter file name: ")

        
if len(fname) < 1:
    fname = "8_5_input.txt"

fh = open('/home/gianluca/Projects/PyhtonForEverybody/ch8_Lists/8_5_input.txt')
count = 0


for line in fh:
    if not line.startswith("From ") : continue 
    words = line.split()
    if len(words) < 1 : continue
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
