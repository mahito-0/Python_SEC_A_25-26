import copy
import pandas


a = 5

print(type(a))


b = [1, 2, 3]
c = b
c.append(4)
print(b)
print(c)

d = 10
d = d + 5
print(d)


print(id(b))
print(id(c))

# Using copy to create a shallow copy
r = b.copy()
print(id(r))

s = [[1, 2], [3, 4]]
t = copy.deepcopy(s) # Using deepcopy to create a deep copy
s[0].append(5)
print(s)
print(t)
print(id(s[0]))
print(id(t[0]))
print(id(s))
print(id(t))