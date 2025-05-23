def sort_file_names(files: list[str]) -> list[str]:
  header = []
  head = []
  number = []
  jud = [chr(x) for x in range(97, 123)]
  for index in files:
    header.append(index.split('.')[0].lower())
  ind = []
  for index in range(len(header)):
    pos = 0
    for ini in header[index]:
      if ini not in jud:
        break
      pos += 1
    ind.append(pos)
  for index in range(len(header)):
    head.append(header[index][0:ind[index]])
    number.append(header[index][ind[index]:])
  mapping = {}
  for index in range(len(header)):
    mapping[index] = (head[index], int(number[index]))
  #mapping = sorted(mapping.items(), key=lambda x : x[1][1])
  mapping = sorted(mapping.items(), key=lambda x : (x[1][0], x[1][1]))
  #FOR SORTING
  return [files[mapping[i][0]] for i in range(len(mapping))]

print(sort_file_names(["img12.png", "img10.png", "img2.png", "img1.png", "IMG01.GIF", "img2.JPG"]))