from sys import argv

sum_of_ids = 0

max_tile_count = {'red': 12, 'green': 13, 'blue': 14}
           
def read_file():
    with open(argv[1]) as f:
        games = f.readlines()
        games = map(lambda x: x.strip(), games)
        games = filter(lambda x: x != '', games)
        return games


def parse_game(game):
    id_str, draws_str = game.split(':')
    id = int(id_str.split(' ')[1])
    draws = list(map(parse_draw, draws_str.split(';')))
    return [id, draws]


def parse_draw(draw):
    return list(map(parse_color, draw.split(',')))


def parse_color(tile_color):
    count, color = tile_color.strip().split(' ')
    return [color.strip(), int(count)]


def is_draw_invalid(draws):
    tiles_in_draw = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        count = draw[1]
        color = draw[0]
        tiles_in_draw[color] += count

    for color in tiles_in_draw.keys():
        if tiles_in_draw[color] > max_tile_count[color]:
            return True
        
    return False
    
        
    
games = map(parse_game, read_file())

for game in games:
    is_invalid = False 
    
    for draw in game[1]:
        print(f'\tdraw: {draw}', end=' ')
        if is_draw_invalid(draw):
            print('-> invalid')
            is_invalid = True
            break
    print('-> valid')

    if not is_invalid:
        sum_of_ids += game[0]

print(sum_of_ids)