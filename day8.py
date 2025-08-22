def reverse_words(s):
    s = s.strip()
    words = s.split()
    words.reverse()
    result = ' '.join(words)
    return result

test_cases = [
    "the sky is blue",
    " hello world ",
    "a good example",
    " ",
    "word"
]

for test in test_cases:
    print(f'Input: "{test}"')
    print(f'Output: "{reverse_words
