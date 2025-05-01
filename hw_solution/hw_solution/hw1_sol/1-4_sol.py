peop_init = 312033422
day_of_year = 365
sec_of_year = day_of_year * 24 * 60 * 60
current_peop = peop_init
for y in range(1,6):
    
    born = int(sec_of_year/7.0)
    dead = int(sec_of_year/13.0)
    imm = int(sec_of_year/45)
    current_peop = current_peop + born - dead + imm
    print('year',y,':',current_peop,'人')
