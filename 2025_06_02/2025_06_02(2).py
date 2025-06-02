def subsets(nums: list[int]) -> list[list[int]]:
  mid = []
  js = set(mid)
  mid.append(js)
  for index in nums:
    mid.append(set((index,)))
  for _ in range(len(nums)):
    for index in range(len(mid)):
      middle = set(nums) - mid[index]
      if middle in mid:
        continue
      mid.append(middle)
  for _ in range(len(mid)):
    mid.append(list(mid.pop(0)))
  return mid

#IT IS HARDCODING
# def subsets(nums):
#     result = []

#     def backtrack(start, path):
#         result.append(path[:])  # 현재까지의 path를 복사해서 추가
#         for i in range(start, len(nums)):
#             path.append(nums[i])            # 숫자 추가
#             backtrack(i + 1, path)         # 다음 숫자 탐색
#             path.pop()                     # 마지막 숫자 제거하고 백트래킹

#     backtrack(0, [])
#     return result
#it will be work well

print(subsets([1, 2, 3]))