def day3_p1(filename):

    r = 0
    c = 0
    res = 0

    G = []
    with open(filename,"r") as f:
        for l in f.readlines():
            G.append(list(l.strip()))

        while r+1 < len(G):
            c += 3
            r += 1
            if G[r][c%len(G[r])]=='#':
                res += 1
    return res

#Right 1, down 1.
#Right 3, down 1. (This is the slope you already checked.)
#Right 5, down 1.
#Right 7, down 1.
#Right 1, down 2.

def day3_p2(filename):

    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    G = []
    with open(filename,"r") as f:
        for l in f.readlines():
            G.append(list(l.strip()))
    res = 1
    for (dc,dr) in slopes:
        r = 0
        c = 0
        score = 0
        while r+1 < len(G):
            c += dc
            r += dr
            if G[r][c%len(G[r])]=='#':
                score += 1
        res *= score
    return res

if __name__ == '__main__':
    #Part 1 Test
    result = day3_p1("input/day03test.txt")
    print(result)
    #Part 1 Real
    result = day3_p1("input/day03.txt")
    print(result)
    #Part 2 Test
    result = day3_p2("input/day03test.txt")
    print(result)
    #Part 2 Real
    result = day3_p2("input/day03.txt")
    print(result)