def dfs(n: int, x: int, y: int, computers: list[list[int]]) -> int:
  com = computers
  com[x][y] = 0
  for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
    nx = x + dx
    ny = y + dy
    if 0 <= nx < n and 0 <= ny < n and com[nx][ny] == 1:
      dfs(n, nx, ny, com)
#IT WILL BE BETTER
# def dfs(x):
#     visited[x] = True
#     for i in range(n):
#         if computers[x][i] == 1 and not visited[i]:
#             dfs(i)

def count_networks(n: int, computers: list[list[int]]) -> int:
  cnt = 0
  for x in range(n):
    for y in range(n):
      if computers[x][y] == 1:
        dfs(n, x, y, computers)
        cnt += 1
  return cnt

print(count_networks(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]))
print(count_networks(3, [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]))