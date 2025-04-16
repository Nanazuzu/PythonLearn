def most_frequent_char(s: str) -> str:
    dic = {}
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    res = None
    for ch in dic:
        if res is None or dic[ch] > dic[res] or (dic[ch] == dic[res] and ch < res):
            res = ch

    return res


print(most_frequent_char("banana"))
print(most_frequent_char("zebraapple"))
print(most_frequent_char("zzzzyxxx"))