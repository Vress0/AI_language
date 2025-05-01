
inputs = input('please input a sequece of number with space:').split(' ')
inputs = [int(i) for i in inputs]
set1 = set(inputs)
print(set1)

'''
inputs = input().split(' ')
tmp = []
for i in inputs:
    if i not in tmp:
        tmp.append(i)
print(tmp)
'''