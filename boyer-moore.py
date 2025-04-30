#not-yet-made
def searching_string(s: str, d: str) -> int:
    start = 0
    jud = False
    while(start <= len(s) - len(d)):
        checking_start = start
        end = start + len(d)
        str_list = []
        for index in range(start, end):
            str_list.append(s[index])
        found = False
        inter = 0
        check = True
        for index in range(len(d)):
            if str_list[index] != d[index]:
                check = False
        if check:
            jud = True
            break
        for index in range(0, len(d)):
            if str_list[index] == d[-1 * (index + 1)]:
                found = True
                inter = index
        if found:
            start += len(d) - 1 - inter
        else:
            start += len(d)
        if checking_start == start:
            start += 1
    if jud:
        print("Your str starts: ")
        return start
    else:
        print("Miss...")
        return -1
    
print(searching_string("aaaaaaaabcdeaaaaaaaaa", "bcde"))
print(searching_string("nanazuzu", "gun"))
print(searching_string("pythonisgoodtool", "sgo"))