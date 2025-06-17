def is_last_bracket(l: list) -> bool:
  return l[-1] == '('

def bracket_score(s: str) -> int:
  ret = []
  for index in s:
    if index == '(':
      ret.append(index)
    else:
      if ret[-1] == '(':
        ret.pop()
        ret.append(1)
      else:
        tmp = 0
        while not is_last_bracket(ret):
          tmp += ret.pop()
        ret.pop()
        ret.append(tmp * 2)
  return sum(ret)

print(bracket_score("(())"))
print(bracket_score("()()"))
print(bracket_score("(()(()))"))
print(bracket_score("((())(()))"))
print(bracket_score("(()())(())(())"))