string = input("Enter the string")
fl = input("First Letter")
sl = input("Second Letter")
c=0
afl = []
asl = []
for i in string:
    if i == fl:
        afl.append(string.index(i))
for i in string:
    if i == sl:
        asl.append(string.index(i))
for j in afl:
    for k in asl:
        if j > k:
            c+=1
if c==1:
    print("False")
else:
    print("True")





