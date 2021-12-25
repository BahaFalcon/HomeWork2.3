def procent_fun(s1, s2):
    if len(s1) == len(s2):
        s1, s2 = s2, s1
    p = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            p += 1
    return str(int(p / len(s1) * 100)) + '%'


print(procent_fun('dfghjdfghj', 'cvghncvghn'))
