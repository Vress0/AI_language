k = eval(input('Please input a int number between 1 to 15: '))
if k < 1 or k > 15:
    print('The number is not between 1 to 15. You lose!')
else:
    for i in range(1, k+1):
        a = [str(i) for i in range(i, 0,-1)]
        b = [str(i) for i in range(2, i+1)]
        a = ' '.join(a)
        b = ' '.join(b)
        if i > 1:   
            s = a+' '+b
        else:
            s = a
        print('{:^69s}'.format(s))
        