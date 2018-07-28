s = 'hello world'
print(s[1])
print(s[2])
print(s[1:4])
print(s[::2])

print(s.find('o'))
print(s.find('w'))
print(s.replace('l', 'k'))
print(s)

# list methods
a = [1,2,3]
b = [10,20]
c = a + b
print(c)

s = 'a b c d e'
z = s.split()
print(z)

if 'a' in z:
    print("'a' is in z")
else:
    print("'a' is not in z")

for i in z:
    print(i)

q = [1,2,3,-1,-10,0]
print(q)
q.sort()
print(q)
q.reverse()
print(q)
print(q.count(3))
print(q.index(2))
print(len(q))
print(min(q))
print(max(q))