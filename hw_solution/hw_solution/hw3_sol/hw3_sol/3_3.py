inputs = input().split(' ')
inputs = [int(i) for i in inputs]
flag = 0
best = max(inputs)
lowest = min(inputs)
if lowest < 0 or best > 100:
    flag = 1
    print('The scores must be 0~100')
if flag == 0:
    p = 0
    for i in inputs:
        if i >= best - 10:
            print('Student',p,'score is',i,'and grade is A')
        elif i >= best - 20:
            print('Student',p,'score is',i,'and grade is B')
        elif i >= best - 30:
            print('Student',p,'score is',i,'and grade is C')
        elif i >= best - 40:
            print('Student',p,'score is',i,'and grade is D')
        else:
            print('Student',p,'score is',i,'and grade is F')
        p += 1
    
