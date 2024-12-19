with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

game = [x.split(':') for x in rows]

games = []
for i in range(len(game)//4 + 1):
    buttona = game[i*4][1]
    buttona = buttona.split(', ')
    buttona = (int(buttona[0][2:]), int(buttona[1][2:]))

    buttonb = game[i*4 + 1][1]
    buttonb = buttonb.split(', ')
    buttonb = (int(buttonb[0][2:]), int(buttonb[1][2:]))

    prize = game[i*4 + 2][1]
    prize = prize.split(', ')
    prize = (int(prize[0][3:]), int(prize[1][2:]))

    games.append((buttona, buttonb, prize))


def my_eq(buttona, buttonb, prize, p2=False):
    if p2:
        px = prize[0] + 10000000000000
        py = prize[1] + 10000000000000
    else:
        px = prize[0]
        py = prize[1]
    ax, bx = buttona[0], buttonb[0]
    ay, by = buttona[1], buttonb[1]

    b = (ax*py - ay*px)/(ax*by - ay*bx)
    a = (px - bx*b)/ax

    print(a, b)
    if a == int(a) and b == int(b):
        return a, b
    
    return 0, 0
    
p1 = 0      
p2 = 0  
for a, b, p in games:
    na, nb = my_eq(a, b, p)
    p1 += int(na*3 + nb*1)
    na, nb = my_eq(a, b, p, True)
    p2 += int(na*3 + nb*1)

print(p1)
print(p2)
