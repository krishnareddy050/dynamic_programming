N=1000
M=1000
memo=[[-1]*(N) for i in range(M)]

def lcs(s1,s2,n,m):
    if memo[n][m]!=-1:
        return memo[n][m]

    if n==0 or m==0:
        memo[n][m]=0

    else:
        
        if s1[n-1]==s2[m-1]:


            memo[n][m]=1+lcs(s1,s2,n-1,m-1)

        else:
            memo[n][m]=max(lcs(s1,s2,n-1,m),lcs(s1,s2,n,m-1))


    return memo[n][m]


if __name__=="__main__":
    s1="axyz"
    s2="bayz"
    print(lcs(s1,s2,len(s1),len(s2)))


    

    