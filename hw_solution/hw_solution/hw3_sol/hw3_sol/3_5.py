from collections import ChainMap
fruits_prices = {"apple": 0.80, "grape": 0.60, "orange": 0.40}
veggies_prices = {"tomato": 1.80, "pepper": 1.40, "onion": 1.23}
order = {'grape': 4, 'tomato': 10, 'orange': 4, 'pepper':1}

G = ChainMap(fruits_prices, veggies_prices)
total = 0
for k,q in order.items():
    print('{k:<6}: ${vp:.2f} x {q} = ${p:.2f}'.format(k=k, vp=G[k], q=q, p=q*G[k]))
    total += q*G[k]
print('Total: ${:.2f}'.format(total))