try :
    fh = open("/home/gianluca/Projects/PyhtonForEverybody/ch9_Dictionaries/input.txt")
except :
    print("ERROR: No input file!")
    exit

dictionary = dict()

for line in fh : 
    words = line.split()
    for word in words :
        dictionary[word] = dictionary.get(word, 0) + 1

print(dictionary)

for key in dictionary :
    print(key, dictionary[key])
