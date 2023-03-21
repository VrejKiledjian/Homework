nums = [2, 5, 3, 7, 3, 8]
target = 10
solutions = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            solutions.append(nums[i])
            solutions.append(nums[j])
            break
    break
if solutions:
    print(solutions)
else:
    print(None)