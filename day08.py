#import modules here

# File input here
filename = "input/day08.txt"

p1_res = 0
p2_res = 0

#Other Globals
ops = []

#code
with open(filename,"r") as f:
    for line in f.readlines():
        line = line.strip()
        opcode, val = line.split()
        ops.append((opcode, int(val)))
    
def day08_p1():
    a = 0
    pc = 0
    seen = set()
    while True:
        #print(pc,a)
        if pc in seen:
            return a
        
        seen.add(pc)

        oc, v = ops[pc]
        if oc == 'jmp':
            pc+=v-1
        elif oc == 'acc':
            a +=v
        elif oc == 'nop':
            pass

        pc += 1


def x(tape):
    a = 0
    pc = 0
    seen = set()
    while True:
        #print(pc,a)
        if pc in seen:
            return None
        
        seen.add(pc)

        oc, v = tape[pc]
        if oc == 'DONE':
            return a
        elif oc == 'jmp':
            pc+=v-1
        elif oc == 'acc':
            a +=v
        elif oc == 'nop':
            pass

        pc += 1
        
def day08_p2():
    for i, v in enumerate(ops):
        tape = ops[:i] + [("nop",0)] + ops[i + 1:] + [("DONE",0)]
        if x(tape):
            return x(tape)

print("\nPart-1") 
print(day08_p1()) #1584
print("\nPart-2")
print(day08_p2()) #920