with open("input_test2.txt",'r') as f:
    data = f.read()
rows = data.split('\n')


def cpu(A, B, C, program):
    def combo_operand(operand):
        b = None
        if operand < 4:
            b = operand
        elif operand == 4:
            b = A
        elif operand == 5:
            b = B
        else:
            b = C
        return b

    def adv(operand):
        a = A
        b = combo_operand(operand)
        return a // 2**b

    def bxl(operand):
        b = B ^ operand
        return b

    def bst(operand):
        a = combo_operand(operand)
        return a % 8
    
    def bxc(operand):
        return B ^ C
    
    def out(operand):
        operand = combo_operand(operand)
        return str(operand % 8)
    
    i = 0
    output = ""
    program_len = len(program)
    while(i < program_len):
        fst = program[i]
        snd = program[i+1]
        if fst == 0:
            A = adv(snd)
            i += 2
        elif fst == 1:
            B = bxl(snd)
            i += 2
        elif fst == 2:
            B = bst(snd)
            i += 2
        elif fst == 3: 
            #jnz
            if A == 0:
                i += 2
            else:
                i = combo_operand(snd)
        elif fst == 4:
            B = bxc(snd)
            i += 2
        elif fst == 5:
            output += out(snd) + ","
            i += 2
        elif fst == 6:
            B = adv(snd)
            i += 2
        elif fst == 7:
            C = adv(snd)
            i += 2
    return output[:-1]


A = int(rows[0].replace('Register A: ', ''))
B = int(rows[1].replace('Register B: ', ''))
C = int(rows[2].replace('Register C: ', ''))
program = [int(x) for x in rows[-1].replace('Program: ', '').split(',')]

p1 = cpu(A, B, C, program)
print(p1)

lowest_num = 0
for i in range(1_000_000_000_000_000):
    if i % 10000 == 0:
        print("A=", i)
    goal = "2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0"
    p2 = cpu(i, B, C, program)
    if p2 == goal:
        lowest_num = i
        break

print(lowest_num)