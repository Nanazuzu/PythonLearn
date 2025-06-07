class SlidingWindow:
  def __init__(self, k: int):
     self.k = k
     self.ret = []
    
  def add(self, val: int) -> None:
    if self.k <= len(self.ret):
      self.ret.pop(0)
    self.ret.append(val)
    
  def get(self) -> list[int]:
    return self.ret

sw = SlidingWindow(3)
sw.add(1)
sw.add(2)
sw.add(3)
print(sw.get())

sw.add(4)
print(sw.get())

sw.add(5)
print(sw.get())