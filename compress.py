s=input()
prev_c=''
count=0
Out=()
for c in s :
    if c == prev_c:
        count+=1
    else:
        if prev_c!='':
            print((count+1,int(prev_c)), end=" ")
        prev_c=c
        count=0
print((count+1,int(prev_c)),end=" ")