def countways(coin,s,n):
    if s==0:
        return 1

    if s<0:
        return 0

    if n==0:
        return 0

    return countways(coin,s-coin[n-1],n) + countways(coin,s,n-1)


coin=[2,5,3]

print(countways(coin,5,len(coin)))