#--- Day 6: Custom Customs ---
import math

def day6_p1(filename):
    groups = []    
    groups2 = []
    current = set()
    current2 = []
    with open(filename,"r") as f:
        
        for l in f.readlines():
            l = l.strip()
            if l == '':
                #print(current)
                groups.append(current)
                groups2.append(current2)
                current = set()
                current2 = []
            else:
                for c in l:
                    current.add(c)
                current2.append(l)
            
    groups.append(current)
    groups2.append(current2)
    #print(groups)
    res = sum(len(g) for g in groups)

    return res, groups2

def day6_p2(groups):
    s = 0
    #print(groups)
    for g in groups:
        for char in "abcdefghijklmnopqrstuvwxyz":
            no = False
            for p in g:
                if char not in p:
                    no = True
                    break
            if not no:
                s += 1
    return s        

if __name__ == '__main__':
    print("\nPart-1")
    #Part - 1 
    result, groups2 = day6_p1("input/day06.txt")
    print(result) #6633
    print("\nPart-2")
    # #Test Part - 2
    result = day6_p2(groups2)
    print(result) #3202
    print("\nEnjoy the rest of the day! ;)")