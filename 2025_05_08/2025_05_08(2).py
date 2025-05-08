def find_vowel_ending_words(s: str) -> list[str]:
    jud = ['a', 'e', 'i', 'o', 'u']
    st_ls = s.split(" ")
    res = []
    dp = set()
    for index in st_ls:
        mid = index
        if not mid.islower():
            mid = mid.lower()
        if mid[-1] in jud:
            res.append(mid)
    for index in res:
        dp.add(index)
    return sorted(list(dp))

print(find_vowel_ending_words("Apple orange bananA Pear plum") or "None")
print(find_vowel_ending_words("dog cat fish") or "None")