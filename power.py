base=int(raw_input("Enter base: "))
exp=int(raw_input("Enter exponential value: "))
power=1
i=0
if exp==1:
    print "Power=",base
else:
    for i in range(0,exp):
        power=power*base
    print"Power=",power
