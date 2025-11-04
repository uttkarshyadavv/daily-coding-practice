#Multiple Source
def floydWarshall(dist):
    n=len(dist)

    for via in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][via]!= 10**8 and dist[via][j]!=10**8:
                    dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
    return dist