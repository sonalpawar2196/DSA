start = 0
next = 1
length = 20
cnt = 0
fibonacci = []
fibonacci.append(start)
fibonacci.append(next)
while cnt != length - 2:
    sum = next + start
    start = next
    next = sum
    fibonacci.append(sum)
    cnt += 1

print(fibonacci)
print(len(fibonacci))