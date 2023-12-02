with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

game_sum = 0
for row in rows:
    game_id = row.split(':')
    items = game_id[1].split(';')
    
    bag = {'red' : 0, 'green' : 0, 'blue' : 0}
    for item in items:
        item = [a.split() for a in item.split(',')]        
        for bricks in item:
            if int(bricks[0]) > bag[bricks[1]]:
                bag[bricks[1]] = int(bricks[0])

    red, blue, green = bag['red'], bag['blue'], bag['green']
    game_sum += green*blue*red

print(game_sum)
