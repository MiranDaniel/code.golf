f,b="Fizz","Buzz"
for i in range(1,101):print(f+b if i%15<1else(f if i%3<1else(b if i%5<1else i)))
