def longest_palindrome(s):
    if len(s) <= 1:
        return s

    start, max_len = 0, 1

    for i in range(len(s)):
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1

    return s[start:start + max_len]

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("a"))
print(longest_palindrome("aaaa"))
print(longest_palindrome("abc"))
