def degrees_of_five(n, nums):
    count = 0
    for i in nums:
        while i % 5 == 0:
            i //= 5
            if i == 1:
                count += 1
    return count

n = int(input())
nums = list(map(int, input().split()))

print(degrees_of_five(n, nums))