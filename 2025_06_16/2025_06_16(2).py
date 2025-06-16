from collections import deque as d

def inserting(deque: d, s: str) -> d:
  tmp = deque
  for _ in range(len(deque)):
    mid = tmp.popleft()
    for index in s:
      tmp.append(mid + index)
  return tmp

def phone_combinations(digits: str) -> list[str]:
  phone = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
  if digits == "":
    return []
  key = []
  for index in digits:
    key.append(int(index))
  ret = d()
  for index in phone[key[0] - 2]:
    ret.append(index)
  for index in key[1:]:
    inserting(ret, phone[index - 2])
  return sorted(list(ret))

print(phone_combinations("23"))
print(phone_combinations(""))
print(phone_combinations("7"))