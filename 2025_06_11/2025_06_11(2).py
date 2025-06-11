def lis_length(sequence: list[int]) -> int:
  ret = {}
  ret[min(sequence)] = sequence.index(min(sequence))
  for index in sequence[ret[min(sequence)]:]:
    if max(index, list(ret.keys())[-1]) == index:
      ret[index] = sequence.index(index)
  return len(ret.keys())
#USE DP BASED CODE
# def lis_length(sequence: list[int]) -> int:
#     n = len(sequence)
#     dp = [1] * n  # 자기 자신만 LIS일 경우 → 길이 1

#     for i in range(1, n):
#         for j in range(i):
#             if sequence[j] < sequence[i]:
#                 dp[i] = max(dp[i], dp[j] + 1)

#     return max(dp)


print(lis_length([10, 20, 10, 30, 20, 50]))
print(lis_length([5, 2, 7, 4, 3, 8, 6, 9]))
print(lis_length([10, 9, 8, 7, 6]))
print(lis_length([1, 3, 2, 5, 4, 6, 7]))