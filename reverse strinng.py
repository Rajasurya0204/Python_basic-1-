def reverse(s_str):
    a = ""
    for i in range(1, len(s_str) + 1):
        a += s_str[len(s_str) - i]
    return a
s_str = input()
print(reverse(s_str))
