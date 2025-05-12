from random import shuffle

def print_permutations(s: str) -> None:
  mid = []
  for index in s:
    mid.append(index)
  res = []
  cnt = 0
  length = 0
  while(True):
    if cnt > 20 and length == len(set(res)):
      break
    shuffle(mid)
    res.append(''.join(mid))
    length = len(set(res))
    cnt += 1
  print(sorted(list(set(res))))


#This is easier way to use itertools
# from itertools import permutations

# def print_permutations(s: str) -> None:
#     perms = [''.join(p) for p in permutations(s)]
#     for p in sorted(set(perms)):
#         print(p)


print_permutations("abc")
print_permutations("ab")