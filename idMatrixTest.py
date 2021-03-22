from time import time

start = time()
def id_mtrx(n):
    id_list = []
    if n >= 0:
        for a in range(n):
            row = [0]*n
            row[a] = 1
            id_list.append(row)
    else:
        n = abs(n)
        for a in range(n):
            row = [0]*n
            row[n-a-1] = 1
            id_list.append(row)
    
    for b in range(len(id_list)):    
        print(id_list[b])
    
    return id_list

for a in range(-10,10):
    id_mtrx(a)
    print("\n")


print(time()-start)