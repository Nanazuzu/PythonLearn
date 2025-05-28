def mix_scoville(scoville: list[int], K: int) -> int:
  ret = 0
  done = False
  scos = scoville
  while(len(scos) != 1):
    jud = sorted(scos)
    if K <= jud[0]:
      done = True
      break
    low = jud.pop(1)
    lower = jud.pop(0)
    jud.append(lower + low * 2)
    scos = jud
    ret += 1
  if done:
    return ret
  else:
    return -1
  
#HEAPQ WILL BE FASTER
# import heapq

# def mix_scoville(scoville, K):
#     heapq.heapify(scoville)
#     count = 0
#     while scoville[0] < K:
#         if len(scoville) < 2:
#             return -1
#         low1 = heapq.heappop(scoville)
#         low2 = heapq.heappop(scoville)
#         heapq.heappush(scoville, low1 + low2 * 2)
#         count += 1
#     return count

print(mix_scoville([1, 2, 3, 9, 10, 12], 7))
print(mix_scoville([1, 1, 1, 1], 10))
print(mix_scoville([10, 12, 3, 9, 2], 20))
print(mix_scoville([7, 8, 10], 7))