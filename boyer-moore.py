def build_bad_char_table(pattern: str) -> dict: #last index
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def searching_string(s: str, d: str) -> int:
    bad_char_table = build_bad_char_table(d)
    m = len(d)
    n = len(s)
    shift = 0 #sliding start

    while shift <= n - m:
        j = m - 1  # pattern check
        while j >= 0 and d[j] == s[shift + j]:
            j -= 1

        if j < 0:
            print("Your str starts: ")
            return shift

        # s[shift + j]
        fail_char = s[shift + j]
        # bad_char_table check
        if fail_char in bad_char_table:
            last_occurrence = bad_char_table[fail_char]
            skip = max(1, j - last_occurrence)
        else:
            skip = j + 1  # skip for all

        shift += skip

    print("Miss...")
    return -1
    
print(searching_string("aaaaaaaabcdeaaaaaaaaa", "bcde"))
print(searching_string("nanazuzu", "gun"))
print(searching_string("pythonisgoodtool", "sgo"))