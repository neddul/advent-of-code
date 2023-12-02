with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

game_sum = 0

for row in rows:
    game_id = row.split(':')
    items = game_id[1].split(';')
    info = []
    for item in items:
        item = [a.split() for a in item.split(',')]
        info.append(item)

    bag = {'red' : 0, 'green' : 0, 'blue' : 0}
    valid_game = True
    for item_set in info:
        for item in item_set:
            if int(item[0]) > bag[item[1]]:
                bag[item[1]] = int(item[0])
    
    red = bag['red']
    blue = bag['blue']
    green = bag['green']

    game_sum += green*blue*red

print(game_sum)
