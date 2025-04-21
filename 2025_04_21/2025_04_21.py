def is_valid_parentheses(s: str) -> bool:
  l_list = []
  for digit in s:
    if digit == '(':
      l_list.append(1)
    elif digit == '{':
      l_list.append(2)
    elif digit == '[':
      l_list.append(3)
    else:
      if digit == ')' and l_list[-1] == 1:
        l_list.pop()
      elif digit == '}' and l_list[-1] == 2:
        l_list.pop()
      elif digit == ']' and l_list[-1] == 3:
        l_list.pop()
      else:
        break
  if len(l_list) > 0:
    return False
  else:
    return True
  
print(is_valid_parentheses("([{{()}}])"))
print(is_valid_parentheses("(}"))
print(is_valid_parentheses("({({([[()]])})})"))