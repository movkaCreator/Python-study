def degrees_of_five(n, nums):
    count = 0
    for i in range(n):
        if nums[i] == 1:
            count += 1
            continue
        while nums[i] % 5 == 0:
            nums[i] /= 5
            if nums[i] == 1:
                count += 1
    return count

n = int(input())
nums = list(map(int, input().split()))

print(degrees_of_five(n, nums))