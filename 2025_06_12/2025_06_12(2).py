def reverse_words_with_tags(s: str) -> str:
  is_tag = False
  ret = []
  mid = []
  for index in s:
    if index == '<':
      is_tag = True
      if len(mid) != 0:
        ret.append(''.join(mid))
        mid.clear()
      mid.append('<')
      continue
    elif index == '>':
      is_tag = False
      mid.append('>')
      ret.append(''.join(mid))
      mid.clear()
      continue
    if index == ' ':
      mid.append(' ')
      ret.append(''.join(mid))
      mid.clear()
      continue
    if is_tag:
      mid.append(index)
    elif not is_tag:
      mid.insert(0, index) #IT CAN BE ret.append(''.join(mid[::-1]))
  if len(mid) != 0:
    ret.append(''.join(mid))
  return ''.join(ret)

print(reverse_words_with_tags("baekjoon online judge"))
print(reverse_words_with_tags("<open>tag<close>"))
print(reverse_words_with_tags("one1 two2 three3 4fourr <hello> world"))