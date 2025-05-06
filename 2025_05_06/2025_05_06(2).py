def longest_digit_sequence(s: str) -> str:
  num_list = []
  jud = [str(x) for x in range(10)]
  dis = {}
  for index in s:
    if index in jud:
      num_list.append(index)
    elif len(num_list) != 0:
      number = ''.join(num_list)
      leng = len(number)
      dis[number] = leng
      num_list.clear()
  if len(num_list) != 0:
    number = ''.join(num_list)
    leng = len(number)
    dis[number] = leng
    num_list.clear()
  if len(dis.keys()) == 0:
    return "None"
  res = list(dis.keys())[0]  #dictionary keys() function's return value IS NOT LIST, IT'S VIEW OBJECT!
  for index in list(dis.keys()):
    if dis[res] < dis[index]:
      res = index
  return res

print(longest_digit_sequence("abc1234de56789fgh12"))
print(longest_digit_sequence("abc12de3456fgh78"))
print(longest_digit_sequence("abcdefg"))