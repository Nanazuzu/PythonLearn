def count_unique_letters(s: str) -> int:
    if len(s) == 0:
        return 0
    str_set = set(s)
    lfs = []
    for index in str_set:
        lfs.append(index)  # HAVE NOT TO USE LIST.
    print(sorted(lfs))
    return len(lfs)

print(count_unique_letters("applepie"))
print(count_unique_letters("banana"))
print(count_unique_letters("nanazuzu"))
print(count_unique_letters(""))