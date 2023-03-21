n = [1, 2, 4, 3]
sorted_n = []
duplicates = []
for num in n:
    if num not in sorted_n:
        sorted_n.append(num)
    else:
        duplicates.append(num)
if duplicates:
    print(duplicates)
else:
    print(None)