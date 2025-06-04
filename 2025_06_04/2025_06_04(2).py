def largest_square(grid: list[list[int]]) -> int:
  x = len(grid)
  y = len(grid[0])
  dp = [[0] * y for _ in range(x)]
  max_size = 0
  for i in range(x):
    for j in range(y):
      if grid[i][j] == 1:
        if i == 0 or j == 0:
          dp[i][j] = 1
        else:
          dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        max_size = max(max_size, dp[i][j])
  return max_size

print(largest_square([
    [1, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 1]
]))
print(largest_square([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
))