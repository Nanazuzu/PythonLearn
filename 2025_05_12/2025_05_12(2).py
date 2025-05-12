def delete_prim(s: str) -> str:
  res = []
  for index in range(len(s)):
    if index == 0 or index == 1:
      continue
    res.append(s[index])
  return ''.join(res)

def convert_number_bases(n: int) -> str:
  res = []
  h = hex(n)
  o = oct(n)
  b = bin(n)
  res.append(delete_prim(h))
  res.append(delete_prim(o))
  res.append(delete_prim(b))
  #easier way : ex)  hex(n)[2:]
  return ' '.join(res)

print(convert_number_bases(255))
print(convert_number_bases(10))
print(convert_number_bases(0))