#97, 122 25
def mirror_string(string: str) -> str:
  mir_string = ""
  for index in range(len(string)):  # MORE EASIER -> chr(219 - ord(string[index]))
    dist = ord(string[index]) - 109
    dist *= -1
    mir_string += chr(110 + dist)
  return mir_string

print(mirror_string("abcxyz"))
print(mirror_string("nanazuzu"))