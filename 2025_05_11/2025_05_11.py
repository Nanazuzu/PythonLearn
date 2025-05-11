def remove_parentheses_content(s: str) -> str:
  msg = s
  is_bucket = False
  res = []
  for index in msg:
    if index == '(':
      is_bucket = True
      continue
    elif index == ')':
      is_bucket = False
      continue
    if not is_bucket:
      res.append(index)
  return ''.join(res)

print(remove_parentheses_content("hello (this should be removed) world"))
print(remove_parentheses_content("keep this (remove) and this (too)"))
print(remove_parentheses_content("no brackets here"))