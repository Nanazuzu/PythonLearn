def max_lan_length(cables: list[int], k: int) -> int:
  start = 1
  end = max(cables)
  ret = 0
  while start <= end:
    mid = (start + end) // 2
    cnt = sum(cable // mid for cable in cables)
    if cnt >= k:
      ret = mid
      start = mid + 1
    else:
      end = mid - 1
  return ret

print(max_lan_length([802, 743, 457, 539], 11))