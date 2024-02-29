prev = 0
next = 1
print(prev, end=" ")
print(next, end=" ")

count = 2

def fibonacci(prev, next):
    global count
    if count != 20:
        sum = prev + next
        prev = next
        next = sum
        count += 1
        print(sum, end=" ")
        fibonacci(prev, next) 
    else:
        return
    
fibonacci(0, 1)