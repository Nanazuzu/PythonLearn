def shortest_compression_length(s: str) -> int:
  if len(s) == 1:
    return 1
  min_len = len(s)
  for index in range(1, len(s) // 2 + 1):
    string = ''
    pre = s[:index]
    cnt = 1
    for i in range(index, len(s), index):
      same = s[i:i+index]
      if same == pre:
        cnt += 1
      else:
        if cnt != 1:
          string += str(cnt) + pre
        else:
          string += pre
        pre = same
        cnt = 1
    if cnt != 1:
      string += str(cnt) + pre
    else:
      string += pre
    min_len = min(min_len, len(string))
  return min_len

print(shortest_compression_length("aabbaccc"))
print(shortest_compression_length("abcabcdede"))