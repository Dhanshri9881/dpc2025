def get_permutations(s):
    def backtrack(path,used):
        if len(path)==len(chars):
         result.append("".join(path))
         return
        for i in range(len(chars)):
            if used[i]:
                continue
            if i>0 and chars[i]==chars[i-1]and not used[i-1]:
                continue
            used[i]=True
            path.append(chars[i])
            backtrack(path,used)
            path.pop()
            used[i]=False
    chars=sorted(list(s))
    result=[]
    backtrack([],[False]*len(chars))
    return result
print(get_permutations("abc"))
print(get_permutations("aab"))
print(get_permutations("aaa"))
print(get_permutations("a"))
print(get_permutations("abcd"))

