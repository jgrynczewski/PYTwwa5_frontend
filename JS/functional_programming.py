def f(x):
    return x**2

print(f(4))

g = lambda x: x*2
print(g(4))

results = []
for item in range(1, 11):
    if f(item) > 50:
        results.append(f(item))
print(results)

print(list(filter(lambda x:x > 50, map(lambda x: x**2, range(1,11)))))

#map
print(list(map(lambda x: x**2, range(1,11))))

# filter
def f2(x):
    if x % 2 == 0 :
        return True
    else:
        return False


print(list(filter(f2, [1,2,3,4,5,6])))
print(list(filter(lambda x: not x%2, [1, 2, 3, 4, 5, 6])))

x = [[1,2], [7,8], [2,45]]

def g(x):
    return x[1]

print(sorted(x, key=g))
print(sorted(x, key=lambda x: (x[0]**2 + x[1]**2)**(0.5)))