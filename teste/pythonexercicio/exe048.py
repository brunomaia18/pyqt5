s = 0
count = 0
for c in range (1,501,2):
    if c % 3 == 0:
        count = count + 1
        s += c 
 
print("A soma de {}  valores foi {}".format(count, s))