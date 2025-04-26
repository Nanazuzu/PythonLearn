def is_all_removed_by_pairing(s: str) -> bool:
  check_list = []
  list_index = 0  #<<it's same with len(check_list)
  for index in s:
    if list_index < 1:  #index starts 0
      check_list.append(index)
      list_index += 1
      continue
    if(check_list[-1] == index):
      check_list.pop()
      list_index -= 1
    else:
      check_list.append(index)
      list_index += 1
  if len(check_list) != 0:
    return False
  else:
    return True
  
print(is_all_removed_by_pairing("abccba"))
print(is_all_removed_by_pairing("abcabc"))
print(is_all_removed_by_pairing("aabbcc"))