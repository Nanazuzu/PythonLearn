from collections import deque as d

def helper(src: str, dst: str) -> bool:
  cnt = 0
  for s, d in zip(src, dst):
    if s != d:
      cnt += 1
  return cnt == 1

def word_ladder(begin: str, target: str, words: list[str]) -> int:
  if target not in words:
    return 0
  vi = set()
  qu = d()
  qu.append((begin, 0))
  while qu:
    cur, dep = qu.popleft()
    if cur == target:
      return dep
    for index in words:
      if index not in vi and helper(cur, index):
        vi.add(index)
        qu.append((index, dep + 1))

print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))