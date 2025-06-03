def is_valid_email(email: str) -> bool:
  bblink = False
  at_split = email.split('@')
  if len(at_split) != 2:
    return False
  elif '' in at_split:
    return False
  jud = [chr(x) for x in range(97, 123)]
  for index in at_split:
    for ind in index:
      if ind not in jud:
        bblink = True
        break
    if bblink:
      break
  if bblink:
    return False
  else:
    return True
  
print(is_valid_email("user@example"))
print(is_valid_email("u@e"))
print(is_valid_email("@example"))
print(is_valid_email("user@"))
print(is_valid_email("user@@example"))
print(is_valid_email("user example@site"))