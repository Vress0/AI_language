num = int(input("請輸入整數: "))
a = []
for d in range(2,num):
    while num % d == 0:
        a.append(d)
        num = num / d
print(a)