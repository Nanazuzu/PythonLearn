def minimize_sum(nums: list[int], k: int) -> int:
  let = sorted(nums, reverse=True)
  for _ in range(k):
    if len(let) == 0:
      break
    let.pop()
  return sum(let)

print(minimize_sum([5, 3, 2, 4, 1], 2))
print(minimize_sum([1, 2, 3], 5))
print(minimize_sum([-1, -2, -3, 4], 1))