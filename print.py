if __name__ == '__main__':
    n = int(input())
    if n not in range(1,151):
        print("n must be a value inclusively between 1 and 150" )
        exit()
    for i in range (1,n+1):
        print(i,end="")