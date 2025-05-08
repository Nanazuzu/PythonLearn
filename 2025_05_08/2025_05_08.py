def longest_word(s: str) -> str:
    st_ls = s.split(" ")
    le_ls = []
    res = []
    dp = set()
    highest = 0
    for index in st_ls:
        le_ls.append(len(index))
        dp.add(len(index))
    for index in le_ls:
        if highest < index:
            highest = index
    cnt = 0
    for index in range(len(le_ls)):
        if highest == le_ls[index]:
            cnt += 1
            res.append(st_ls[index])
    jud = False
    if cnt == 1:
        jud = True
    if jud:
        return res[0]
    res = sorted(res, reverse=True)
    return res[0]

print(longest_word("apple banana cherry dragonfruit egg"))
print(longest_word("blue red green cyan"))
print(longest_word("a ab abc abd abc"))