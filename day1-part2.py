with open('day1.input', 'r') as file: 
    data = [x.strip() for x in file.readlines()]

digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

digits_rev = {k[::-1]: v for k,v in digits.items()}

print(digits_rev)

def try_get_digit(line, rev):
    d = -1

    digits_local = digits_rev if rev == True else digits

    if line[0].isnumeric():
        d = line[0]
    elif line[0:3] in digits_local:
        d = digits_local[line[0:3]]
    elif line[0:4] in digits_local:
        d = digits_local[line[0:4]]
    elif line[0:5] in digits_local:
        d = digits_local[line[0:5]]
    
    return d

s = 0
for line in data: 
    
    for i in range(len(line)):
        d1 = try_get_digit(line[i:], rev=False)
        if d1 != -1: break

    for i in range(len(line)): 
        d2 = try_get_digit(line[::-1][i:], rev=True)
        if d2 != -1: break

    s += (int(str(d1)+str(d2)))

print(s)