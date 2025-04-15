def reverse_words(s: str) -> str:
    digit = s.split(' ')
    result_digit = ""
    for word in digit:
        result_digit += word[::-1] + ' '
    return result_digit.strip()

print(reverse_words("Python is fun"))