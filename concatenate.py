def matrix_printer(arr,n,m):
    for i in range(n):
        if i == 0:
            print('[[' + ' '.join(map(str, arr[0][0:m])) + ']')
        elif i == n-1:
            print(' [' + ' '.join(map(str, arr[n-1][0:m])) + ']]')
        else:
            print(' [' + ' '.join(map(str, arr[i][0:m])) + ']')
                
n,m,p = map(int, input().split())
lst=[]
for _ in range(n+m):
    lst.append(list(map(int,input().split())))

matrix_printer(lst,(n+m),p)