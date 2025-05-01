def jud_move(n:int, cmd:str, pos:list) -> list:
  if cmd == 'U' or cmd == 'D':
    if cmd == 'U':
      if pos[1] == n - 1:
        return pos
      else:
        pos[1] += 1
        return pos
    else:
      if pos[1] == 0:
        return pos
      else:
        pos[1] -= 1
        return pos
  elif cmd == 'L' or cmd == 'R':
    if cmd == 'L':
      if pos[0] == 0:
        return pos
      else:
        pos[0] -= 1
        return pos
    else:
      if pos[0] == n - 1:
        return pos
      else:
        pos[0] += 1
        return pos
def robot_position(n: int, cmds: str) -> tuple[int, int]:
  mid_list = [0,0]
  for index in cmds:
    mid_list = jud_move(n,index,mid_list)
  x = mid_list[0]
  y = mid_list[1]
  return (x,y)

print(robot_position(5, "RRRDDDLLUU"))
print(robot_position(3, "UUUUUUUUUUUURRRRRRRRRRRRLD"))