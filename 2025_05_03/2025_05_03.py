class CircularQueue:
    start = 0
    text = []
    def __init__(self, size: int):
        self.size = size
    def enqueue(self, x: int) -> None:
        if len(self.text) == self.size:
            return
        self.text.append(x)
    def dequeue(self) -> int:
        if len(self.text) == 0:
            return -1
        # text = list(sorted(self.text,reverse=True))
        # res = text.pop()
        # self.text = list(sorted(text,reverse=True))
        # return res
        # MISJUDGED, Not sorted.
        return self.text.pop(0)
    def front(self) -> int:
        if len(self.text) == 0:
            return -1
        return self.text[0]

q = CircularQueue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
q.enqueue(4)
print(q.front())