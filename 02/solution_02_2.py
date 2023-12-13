from sys import argv

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


def get_sum_of_powers(draws):
    power = 1
    for color in ['red', 'green', 'blue']:
        flat_draws = [color for draw in draws for color in draw]
        power *= max(list(map(lambda y: y[1], filter(lambda x: x[0] == color, flat_draws))))

    return power


games = map(parse_game, read_file())
sum_of_powers = 0

for game in games:
    sum_of_powers += get_sum_of_powers(game[1])
    
print(sum_of_powers)