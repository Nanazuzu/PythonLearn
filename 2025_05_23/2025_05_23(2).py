def explode_string(s: str, bomb: str) -> str:
  ret = []
  for index in s:
    ret.append(index)
    if len(ret) < len(bomb):
      continue
    if ''.join(ret)[-len(bomb):] == bomb:  #IT CAN USE if ret[-len(bomb):] == list(bomb)
      for _ in range(len(bomb)):
        ret.pop()
  return ''.join(ret) or "FRULA"

print(explode_string("mirkovC4nizCC44", "C4"))
print(explode_string("12ab112ab2ab", "12ab"))
print(explode_string("aaaa", "aa"))