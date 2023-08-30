from decimal import Decimal,getcontext;q=Decimal;getcontext().prec=1001;y=q(0);z=q(1)
for i in range(1001):a,b,c,d,e=z/(16**i),z*4/(8*i+1),z*2/(8*i+4),z/(8*i+5),z/(8*i+6);r=a*(b-c-d-e);y+=r
print(y)
