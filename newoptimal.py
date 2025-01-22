pages = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
capacity = 3

memory = []
miss = 0
hit = 0

for i in range(len(pages)):
    if pages[i] not in memory:
        miss += 1
        if len(memory) < capacity:
            memory.append(pages[i])
        else:
            future = pages[i+1:]
            furthest = max(memory, key=lambda x: future.index(x) if x in future else float('inf'))
            memory[memory.index(furthest)] = pages[i]
    else:
        hit += 1

print("Total hits:", hit)
print("Total misses:", miss)
print("Hit ratio:", hit / len(pages))
print("Miss ratio:", miss / len(pages))
