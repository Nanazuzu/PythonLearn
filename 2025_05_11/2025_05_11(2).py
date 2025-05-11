def reverse_word_order(s: str) -> str:
  msg = s.split()
  res = []
  for index in msg:
    res.insert(0, index)
  return ' '.join(res)  #It can use easier with
#' '.join(s.split()[::-1])
#This code in return

print(reverse_word_order("this is a test"))
print(reverse_word_order("hello world"))