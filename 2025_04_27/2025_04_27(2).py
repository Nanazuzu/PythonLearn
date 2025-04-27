def final_position(commands: str) -> tuple[int, int]:
  x = 0
  y = 0
  for index in commands:
    if index == 'U':
      y += 1
    elif index == 'D':
      y -= 1
    elif index == 'L':
      x -= 1
    else:
      x += 1
  res = (x,y)
  return res

print(final_position("UUURRR"))
print(final_position("UUDDLRLR"))