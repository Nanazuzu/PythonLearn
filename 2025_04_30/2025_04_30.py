def longest_unique_substring(s: str) -> int:
    start = 0
    end = 1
    window_map = {}
    window_map[s[start]] = start
    dist = 0
    while(True):
        while(True):
            if s[end] in window_map.keys():
                break
            if end + 1 == len(s):
                break
            window_map[s[end]] = end
            end += 1
            if dist < end - start:
                dist = end - start
        while(True):
            if s[start] not in window_map.keys():
                break
            if start + 1 == len(s):
                break
            window_map.pop(s[start])
            start += 1
        if end + 1 == len(s):
            break
    return dist

print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbbb"))
print(longest_unique_substring("pwwkew"))
print(longest_unique_substring("nanazuzu"))
print(longest_unique_substring("acdc"))