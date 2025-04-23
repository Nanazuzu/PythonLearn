def shuffle_blocks_func(s: str) -> str:
  mid = []
  ret = []
  for index in range(0, len(s) // 2 + 2, 2):
    freq = s[index] + s[index + 1]
    mid.append(freq)
  cnt = len(mid)
  while(cnt > 0):
    ret.append(mid.pop())
    cnt -= 1
  return ''.join(ret)

def shuffle_blocks(s: str) -> str:
  if len(s) % 2 == 1:
    end_str = s[-1]
    end_str_pop = []
    for index in range(0, len(s) - 1, ):
      end_str_pop.append(s[index])
    end_str_pop_str = ''.join(end_str_pop)
    ret = shuffle_blocks_func(end_str_pop_str)
    ret += end_str
    return ret
  else:
    return shuffle_blocks_func(s)
  
print(shuffle_blocks("abcdef"))
print(shuffle_blocks("abcde"))