import re

with open('day2.input', 'r') as f:
    data = [x.strip() for x in f.readlines()]

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

bad_id_sum = 0 

for line in data: 
    semi_idx = line.index(':')

    game_id = int(line[len('Game:'):semi_idx])

    games = line[semi_idx + 2:].split('; ')

    is_bad = False

    for game in games:
        
        g_search = re.search('(\d+) green', game)
        green = 0 if g_search is None else g_search.group(1)
        if int(green) > MAX_GREEN:
            is_bad = True 
            break
        
        r_search = re.search('(\d+) red', game)
        red = 0 if r_search is None else r_search.group(1)
        if int(red) > MAX_RED: 
            is_bad = True
            break 

        b_search = re.search('(\d+) blue', game)
        blue = 0 if b_search is None else b_search.group(1)
        if int(blue) > MAX_BLUE:
            is_bad = True 
            break


    if not is_bad:
        bad_id_sum += game_id

print(bad_id_sum)