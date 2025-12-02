with open("input.txt",'r') as f:
    data = f.read()
rows = data.split(',')

p1 = 0
p2 = 0

my_set = set()

def test_num(number):
    test = False
    #1 repeating
    num_len = len(number)

    for size in range(1, len(number) + 1):

        if test:
            # print("Returned")
            return int(number)
            

        if size > (num_len/2):
            break

        start = number[:size]
        # print(start)
    

    
        succ = True
        for i in range(size, len(number), size):
            chunk = number[i:i+size]
            # print(number, start, chunk)
            if chunk != start:
                succ = False
                test = False
                
            
            # print(succ)
        
            if succ:
                test = True
        
        
    return 0

for row in rows:
    start, stop = row.split('-')
    for i in range(int(start), int(stop)+1):
        if len(str(i)) > 1:
            start_half = str(i)[:int((len(str(i))/2))]
        else:
            start_half = str(i)

        t_id = int(start_half*2)
        # print(start_half, t_id)

        # print(t_id)
        if t_id >= int(start) and t_id <= int(stop):
            # print(t_id)
            my_set.add(t_id)
        
        # print(i)
        p2 += test_num(str(i))
        
        # if ans != 0:
        #     print(ans)

print(p2)