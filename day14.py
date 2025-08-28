def count_substrings_with_k_distinct(s, k):
    def at_most_k_distinct(k):
        count = {}
        left = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            result += (right - left + 1)
        return result
    if k > len(s): 
        return 0
    return at_most_k_distinct(k) - at_most_k_distinct(k - 1)
print(count_substrings_with_k_distinct("pqpqs", 2))
print(count_substrings_with_k_distinct("aabacbebebe", 3))
print(count_substrings_with_k_distinct("a", 1))
print(count_substrings_with_k_distinct("abc", 3))
print(count_substrings_with_k_distinct("abc", 2))
