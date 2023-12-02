import re

with open('day2.input', 'r') as f:
    data = [x.strip() for x in f.readlines()]

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

total = 0 

for line in data: 
    semi_idx = line.index(':')

    game_id = int(line[len('Game:'):semi_idx])

    games = line[semi_idx + 2:].split('; ')

    min_g = min_r = min_b = 0

    for game in games:
        
        g_search = re.search('(\d+) green', game)
        green = 0 if g_search is None else g_search.group(1)
        if int(green) > min_g:
            min_g = int(green)
            
        
        r_search = re.search('(\d+) red', game)
        red = 0 if r_search is None else r_search.group(1)
        if int(red) > min_r: 
            min_r = int(red)
            

        b_search = re.search('(\d+) blue', game)
        blue = 0 if b_search is None else b_search.group(1)
        if int(blue) > min_b:
            min_b = int(blue)
            
    
    power = min_g * min_r * min_b 
    total += power

print(total)