n1 = eval(input('Please input the first number: '))
n2 = eval(input('Please input the second number: '))

if n1 <= n2:
    k = n1
else:
    k = n2

for i in range(k, 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        print(i)
        break 
    