def mystery1(l):
    rv = []
    for x in l:
        rv = [x] + rv
    return rv

print("Result:")
l = [0, 1, 2, 3, 4]
nl = mystery1(l)
print("l: ", l)
print("nl: ", nl)


def mystery2(l):
    rv = []
    for i in range(len(l)-1, -1, -1):
        rv.append(l[i])
    return rv

print("Result:")
l = [0, 1, 2, 3, 4]
nl = mystery2(l)
print("l: ", l)
print("nl: ", nl)


def mystery3(l):
    n = len(l)
    for i in range(n // 2):
        t = l[i]
        l[i] = l[n-i-1]
        l[n-i-1] = t

print("Result:")
l = [0, 1, 2, 3, 4]
mystery3(l)
print("l: ", l)