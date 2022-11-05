m = "hello"


def chat_room():
    x = 0
    s = input()
    for i in range(len(s)):
        if s[i] == m[x]:
            x += 1
        if x == 5:
            return "YES"
    return "NO"


print(chat_room())
