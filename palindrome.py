number=raw_input("Enter a no.")
x=len(number)
i=0
flag=0
for i in range(0,x):
    if number[i]==number[x-i-1]:
        flag=flag+1
if flag==x:
    print"It is a palindrome."
else:
    print"It is not a palindrome."
