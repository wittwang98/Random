from time import time

start = time()

def josephus(n):
    if n == 0: return False
    flag = n%2;
    counter = 0
    index = n-1
    people = [1]*n
    while True:
        if sum(people) == 1:
            return index%n #for pattern finding counter, flag, n]
        elif people[index%n] == 1:
            temp_index = (index%n)+1
            while True:
                if people[temp_index%n] == 1:
                    people[temp_index%n] = 0
                    break
                else:
                    temp_index += 1
        index += 1
        if index%n == 0:
            counter += 1

pattern = []
for a in range(500):
    pattern.append((josephus(a), a))
    
print(pattern)

print(time()-start)
    