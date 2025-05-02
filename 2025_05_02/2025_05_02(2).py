def is_palindrome(s: str) -> bool:
    ans = s.lower()
    jud = []
    for ini in range(97, 123):
        jud.append(chr(ini))
    for ind in range(0, 10):
        jud.append(str(ind))
    # while(True):
    #     brk = False
    #     for index in ans:
    #         if index not in jud and index != "":
    #             brk = False
    #             mid = ans.split(index)
    #             ans = ''.join(mid)
    #         brk = True
    #     if brk:
    #         break
    # IT COURSE INFINITE LOOP
    # down is same algorithm but SAFE

    while True:
        new_ans = ''.join([ch for ch in ans if ch in jud])
        if new_ans == ans:
            break
        ans = new_ans

    for index in range(0, len(ans) // 2):
        if ans[index] != ans[-1 * index - 1]:
            return False
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(""))