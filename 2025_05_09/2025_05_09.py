def sort_words_by_number(s: str) -> list[str]:
    jud_a = [chr(x) for x in range(97,123)]
    jud_n = [str(x) for x in range(10)]
    res = []
    res_n = []
    syn = s.split(' ')
    for index in syn:
        if not index.islower():
            index = index.lower()
        bjud_a = False
        bjud_n = False
        mid = []
        for ini in index:
            if ini in jud_a:
                bjud_a = True
            elif ini in jud_n:
                bjud_n = True
                mid.append(ini)
        if len(mid) == 0:
            continue
        ret = int(''.join(mid))
        if bjud_n and bjud_a:
            if len(res_n) == 0:
                res.append(index)
                res_n.append(ret)
            else:
                inputed = False
                for ind in range(len(res_n)):
                    if ret < res_n[ind]:
                        res.insert(ind, index)
                        res_n.insert(ind, ret)
                        inputed = True
                        break
                if not inputed:
                    res.append(index)
                    res_n.append(ret)
    return res

print(sort_words_by_number("a1b2 x99 7seven hello42 code abc") or "None")