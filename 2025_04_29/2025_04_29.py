def compress_sequence(nums: list[int]) -> list[int]:
    res = []
    cnt = 0
    res.append(nums[cnt])
    for index in nums:
        if res[cnt] == index:  #cnt can chage res[-1]
            continue
        res.append(index)
        cnt += 1
    return res

print(compress_sequence([1,1,2,2,2,3,3,4,4,4,1]))
print(compress_sequence([4,4,4,4]))
print(compress_sequence([1,2,3,4,5]))