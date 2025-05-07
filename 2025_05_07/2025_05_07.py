def most_common_letter(s: str) -> str:
  msg = s
  jud = [chr(x) for x in range(97, 123)]
  if not msg.islower():
    msg = msg.lower()
  cnt = {}
  for index in msg:
    if index in jud:
      if index not in cnt.keys():
        cnt[index] = 1
      else:
        cnt[index] += 1
  res = list(cnt.keys())[0]
  for ini in cnt.keys():
    if cnt[res] < cnt[ini]:
      res = ini
    elif cnt[res] == cnt[ini]:
      if ord(res) < ord(ini):
        continue
      else:
        res = ini
  return res

print(most_common_letter("Hello world! 123 HeLLo!!"))
print(most_common_letter("AaBbCc"))
print(most_common_letter("Nanazuzu"))