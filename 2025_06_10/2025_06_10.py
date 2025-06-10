def card_merge(n: int, m: int, cards: list[int]) -> int:
  card = sorted(cards)
  for _ in range(m):
    x, y = card[0], card[1]
    card[0], card[1] = x + y, x + y
    card = sorted(card)
  return sum(card)

#IT CAN BE FASTER WITH HEAPQ
# import heapq

# def card_merge(n: int, m: int, cards: list[int]) -> int:
#     heapq.heapify(cards)
#     for _ in range(m):
#         x = heapq.heappop(cards)
#         y = heapq.heappop(cards)
#         heapq.heappush(cards, x + y)
#         heapq.heappush(cards, x + y)
#     return sum(cards)


print(card_merge(3, 1, [3, 1, 2]))
print(card_merge(4, 2, [4, 2, 3, 1]))