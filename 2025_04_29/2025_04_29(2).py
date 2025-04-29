def min_jumps(nums: list[int]) -> int:
    opt = 0
    jpd = 0
    while(True):
        if len(nums) - 1 <= opt:
            break
        jud = 0
        opt_sum = 0
        for index in range(1, nums[opt] + 1):
            if len(nums) - 1 <= opt + index: #For IndexError
                opt_sum = index
                break
            if jud < nums[opt + index]:
                jud = nums[opt + index]
                opt_sum = index
        opt += opt_sum #Not jud, use index
        jpd += 1
    return jpd

print(min_jumps([2,3,1,1,4]))
print(min_jumps([1,1,1,1]))
print(min_jumps([3,2,1,4,2,2,3,1]))