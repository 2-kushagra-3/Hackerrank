def solve(string):
    s=""
    space=True
    for x in string :
        if space and x!=' ':
            s=s+x.upper() 
            space=False
        elif x==' ':
            s=s+x
            space=True
        else :
            s=s+x
                    
    return s 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()