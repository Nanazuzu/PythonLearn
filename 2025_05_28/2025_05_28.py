def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
  if sum(gas) < sum(cost):
    return -1
  gases = gas
  costs = cost
  ret = 0
  while True:
    fuel = 0
    circuit = True
    for gased, costed in zip(gases, costs):
      fuel += gased - costed
      if fuel < 0:
        circuit = False
        break
    if not circuit:
      ret += 1
      gases.append(gases.pop(0))
      costs.append(costs.pop(0))     
    else:
      break
  return ret
#IT TAKES O(n^2)
# def can_complete_circuit(gas, cost):
#     total, curr, start = 0, 0, 0
#     for i in range(len(gas)):
#         total += gas[i] - cost[i]
#         curr += gas[i] - cost[i]
#         if curr < 0:
#             start = i + 1
#             curr = 0
#     return start if total >= 0 else -1
#this can be faster

print(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]))
print(can_complete_circuit([2,3,4], [3,4,3]))