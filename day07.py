#--- Day 7: Handy Haversacks ---

from collections import deque

filename = "input/day07.txt"

p1_res = 0
p2_res = 0

required = 'shinygoldbag'

E = {}

with open(filename,"r") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            words = line.split()
            container = words[0]+words[1]+words[2]
            container = container[:-1]
            if words[-3] == 'no':
                continue
            else:
                idx = 4
                while idx < len(words):
                    bag = words[idx]+words[idx+1]+words[idx+2]+words[idx+3]
                    if bag.endswith('.'):
                        bag = bag[:-1]
                    if bag.endswith(','):
                        bag = bag[:-1]
                    if bag.endswith('s'):
                        bag = bag[:-1]
                    while any ([bag.startswith(d) for d in "0123456789"]):
                        bag = bag[1:]
                    if bag not in E:
                        E[bag] = []
                    E[bag].append(container)
                    #print(container, bag, words)
                    idx += 4

SEEN = set()
Q= deque([required])
while Q:
    x = Q.popleft()
    #print(x)
    if x in SEEN:
        continue
    SEEN.add(x)
    for y in E.get(x, []):
        Q.append(y)
print(f"Part-1 result: {len(SEEN)-1}") #P1 result - 131

# reinitialize the set to empty set
E = {}
with open(filename,"r") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            words = line.split()
            container = words[0]+words[1]+words[2]
            container = container[:-1]
            if words[-3] == 'no':
                continue
            else:
                idx = 4
                while idx < len(words):
                    bag = words[idx]+words[idx+1]+words[idx+2]+words[idx+3]
                    if bag.endswith('.'):
                        bag = bag[:-1]
                    if bag.endswith(','):
                        bag = bag[:-1]
                    if bag.endswith('s'):
                        bag = bag[:-1]
                    n = int(bag[0])
                    assert bag[1] not in '0123456789'
                    while any ([bag.startswith(d) for d in "0123456789"]):
                        bag = bag[1:]
                    if container not in E:
                        E[container] = []
                    E[container].append((n,bag))
                    #print(container, bag, words)
                    idx += 4

def size(bag):
    ans = 1
    for (n,y) in E.get(bag, []):
        ans += n*size(y)
    return ans
    
#Part-2 result: 11261
print(f"Part-2 result: {size(required)-1}") 