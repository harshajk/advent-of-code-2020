#--- Day 5: Binary Boarding ---
import math

def day5_p1(filename):
    max_sid = 0    
    sids = set()
    with open(filename,"r") as f:
        for l in f.readlines():
            bf = l[:7]
            lr = l[7:]

            low, hi = 0, 127
            for d in bf:
                m = math.ceil(low + (hi-low)/2)
                if d == 'B':
                    low = m
                else:
                    hi = m

            row = low

            low, hi = 0, 7
            for d in lr:
                m = math.ceil(low + (hi-low)/2)
                if d == 'R':
                    low = m
                else:
                    hi = m
            
            col = low
            sid = row * 8 + col
            #print(sid)                
            if sid > max_sid:
                max_sid = sid
            
            sids.add(sid)

    return max_sid, sids

def day5_p2(sids):
    for i in range(max(sids) + 1):
        if i - 1 in sids and i - 1 in sids and i not in sids:
            return i

if __name__ == '__main__':
    print("\nPart-1")
    #Test Part - 1 
    result, sids_test = day5_p1("input/day05test.txt")
    print(result)
    #Real Part - 1
    result, sids = day5_p1("input/day05.txt")
    print(result)

    print("\nPart-2")
    #Test Part - 2
    print(day5_p2(sids_test))
    #Real
    print(day5_p2(sids))
    print("\nEnjoy the rest of the day, or get set for the next challenge! ;)")