x = 7
y = 5.0
z = 10.0
w = x % 2 + y / z + z + y / (z + z)
print(w)

c = True
d = False
c = c and d
c = not c or d
print(c)

d = 0
for p in range(0, 5):
    if p % 4 == 0:
        d = d + (p-1) * 25;
    else:
        d = d + 100;
print("$" + str(d//100) + "." + str(d % 100))

def F1(i, j) :
    print(f"F1({i}, {j})")
    F2(j, i+j)
    print(f"F1: i = {i}, j = {j}")
    

def F2(i, j) :
    print(f"    F2({i}, {j})".format(i, j))
    k = F3(i, j)
    print(f"    F2: i = {i}, j = {j}, k = {k}")
    

def F3(i, j) :
    print(f"        F3({i}, {j})".format(i, j))
    i = i+j
    j = i+2*j
    k = 2*i+3*j
    print(f"        F3: i = {i}, j = {j}, k = {k}")
    return k
    

print("Result:")
F1(1, 1)
print()