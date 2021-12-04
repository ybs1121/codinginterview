nums = [2, 7, 11, 15]
target = 9

#1
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print("%d , %d"%(i,j))

#2
for i, n in enumerate(nums):
    complement = target - n

    if complement in nums[i+1:]:
        print("%d , %d"%(nums.index(n),nums[i +1 : ].index(complement) + i + 1))


#3
nums_maps = {}
for i, num in enumerate(nums):
    if target - num in nums_maps:
        print("%d , %d"%(nums_maps[target - num], i))

    nums_maps[num] = i
