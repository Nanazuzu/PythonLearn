def visualize_word_length_frequency(s: str) -> None:
  string = s.lower()
  jud = [chr(x) for x in range(97,123)]
  st = string.split(' ')
  stris = []
  for index in st:
    ad = []
    for ind in index:
      if ind not in jud:
        continue
      ad.append(ind)
    stris.append(''.join(ad))
  ret = {}
  for index in stris:
    if len(index) not in ret.keys():
      ret[len(index)] = 1
    else:
      ret[len(index)] += 1
  s_ret = list(sorted(ret.items()))
  for index in s_ret:
    print(f"{index[0]}: {'#' * index[1]}")

visualize_word_length_frequency("Hello world! This is a test, isn't it?")