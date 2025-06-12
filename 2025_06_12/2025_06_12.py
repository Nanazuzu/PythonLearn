def sigma_square(n: int) -> int:
  #sum with square
  #this is sample
  # return (n * (n + 1) * (2 * n + 1))//6
  nums = []
  for index in range(1, n + 1):
    nums.append(index ** 2)
  return sum(nums)

print(sigma_square(3))
print(sigma_square(5))