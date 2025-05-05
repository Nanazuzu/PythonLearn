def extract_and_sort_numbers(s: str) -> list[int]:
  jud = [str(x) for x in range(10)]
  lst = []
  mid_num =[]
  for index in s:
    if index in jud:
      mid_num.append(index)
    elif len(mid_num) != 0:
      sums = 0
      while(len(mid_num) != 0):
        sums += int(mid_num.pop(0)) * (10 ** (len(mid_num)))
      lst.append(sums)
  #It can't handle with ending numbers, so must add this code
  if len(mid_num) != 0:
        sums = 0
        while len(mid_num) != 0:
            sums += int(mid_num.pop(0)) * (10 ** len(mid_num))
        lst.append(sums)
  #Until here.
  return lst

print(extract_and_sort_numbers("a12bc34d5") or "None")
print(extract_and_sort_numbers("abcd") or "None")