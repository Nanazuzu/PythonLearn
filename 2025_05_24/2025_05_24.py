def dfs(x: int, y: int, grid: list[list[str]]):
  gri = grid
  gri[x][y] = '0'
  for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    nx = x + dx
    ny = y + dy
    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
      dfs(nx, ny, gri)

def count_islands(grid: list[list[str]]) -> int:
  cnt = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '1':
        dfs(i, j, grid)
        cnt += 1
  return cnt

print(count_islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))