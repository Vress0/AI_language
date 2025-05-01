D = {}
inputs = input('Enter integers between 1 and 100:').split(' ')
flag = 0
for i in inputs:
    if int(i) < 1 or int(i) > 100:
        print('Invalid input')
        flag = 1
        break
    if i not in D:
        D[i] = 1
    else:
        D[i] += 1
if flag == 0:
    for i in D.keys():
        if D[i] > 1:
            print(i, 'occurs',D[i], 'times')
        else:
            print(i, 'occurs',D[i], 'time')