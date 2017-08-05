number=raw_input("enter a no.")
n=int(number)
i=2
flag=0
for i in range(2,n/2):
    if n%i==0:
        flag=1
        break
if flag==0:
    print"It is a prime no."
else:
    print"It is not a prime no."
