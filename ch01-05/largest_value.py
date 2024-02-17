numbers = [1,4,8,43,5,78,12,33,39,64,56,481,545,138,187,164,134,1,345,3,4,3,4,1,84,54,5,5,4]
largest_so_far = -1

print("Before:", largest_so_far)

for num in numbers:
    if num > largest_so_far:
        largest_so_far = num
        print("canged")
    print(largest_so_far, num)

print("Largest number is", largest_so_far)