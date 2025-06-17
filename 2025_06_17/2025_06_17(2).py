def snail_matrix(n: int) -> list[list[int]]:
  ret = [[0] * n for _ in range(n)]
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  dis = 0
  x,y = 0, 0
  for index in range(1, n * n + 1):
    ret[y][x] = index
    nx = x + dx[dis]
    ny = y + dy[dis]
    if nx < 0 or n <= nx or ny < 0 or n <= ny or ret[ny][nx] != 0:
      dis = (dis + 1) % 4
      nx = x + dx[dis]
      ny = y + dy[dis]
    x, y = nx, ny
  return ret

print(snail_matrix(3))
print(snail_matrix(4))