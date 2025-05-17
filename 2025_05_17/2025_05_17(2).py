def flip_bits(s: str) -> str:
  ret = []
  for index in s:
    if index == '0':
      ret.append('1')
    else:
      ret.append('0')
  return ''.join(ret)

# It can use dictionary
# def flip_bits(s: str) -> str:
#     table = {'0': '1', '1': '0'}
#     return ''.join(table[ch] for ch in s)

print(flip_bits("1010"))
print(flip_bits("0000"))
print(flip_bits("00001111"))