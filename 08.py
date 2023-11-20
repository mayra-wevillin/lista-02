p1=float(input('digite o preco do produto'))
p2=float(input('digite o preco do produto'))
p3=float(input('digite o preco do produto'))
if p1<p2 and p1<p3:
    print('o melho produto para ser comprado e',p1)
elif p2<p1 and p2<p3:
     print('o melho produto para ser comprado e',p2)
else:
     print('o melho produto para ser comprado e',p3)