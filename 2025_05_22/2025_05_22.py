def select_passed_students(records: list[tuple[str, int]]) -> list[str]:
  mid = []
  for index in records:
    if index[1] < 60:
      continue
    mid.append(index)
  sor = sorted(mid, key=lambda x : x[1] ,reverse=True)
  ret = []
  for index in sor:
    ret.append(index[0])
  return ret

print(select_passed_students([("Alice", 58), ("Bob", 75), ("Charlie", 90), ("Diana", 59)]))
print(select_passed_students([("Eve", 61), ("Frank", 60), ("Grace", 95)]))
print(select_passed_students([("Henry", 30), ("Ivy", 40)]))