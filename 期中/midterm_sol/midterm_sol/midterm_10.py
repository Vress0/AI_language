def get_odds(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

for i, odd in enumerate(get_odds(6)):
    if i == 2:
        print('The third odd number is',odd)