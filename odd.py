lower=int(raw_input("Enter the lower interval"))
upper=int(raw_input("Enter the upper interval"))
for i in range(lower,upper+1):
    if i%2!=0:
        print(i)
