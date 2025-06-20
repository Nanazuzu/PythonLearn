def max_valid_parentheses(s: str) -> int:
  tmp = [-1]
  ret = 0
  for i, index in zip(range(len(s)), s):
    if index == '(':
      tmp.append(i)
    else:
      tmp.pop()
      if not tmp:
        tmp.append(i)
      else:
        ret = max(ret, i - tmp[-1])
  return ret

print(max_valid_parentheses("(()"))
print(max_valid_parentheses(")()())"))
print(max_valid_parentheses("((()))"))