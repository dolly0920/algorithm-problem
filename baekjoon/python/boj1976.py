import sys

sys.stdin = open("input.txt", "rt")

def find(x) :
    if x == parent[x] :
        return x
    y = find(parent[x])
    return y

def union(x, y) :
    root1 = find(x)
    root2 = find(y)

    if root1 != root2 :
        if rank[root1] > rank[root2] :
            parent[root2] = root1
        else :
            parent[root1] = root2
            if rank[root1] == rank[root2] :
                rank[root2] += 1
    return

if __name__ == "__main__" :
    N = int(input()) ## 도시의 수
    M = int(input()) ## 여행 계획에 속한 도시의 수
    parent = list(range(N))
    rank = [0] * (N)
    for i in range (N) :
        tmp = list(map(int, input().split()))
        for j in range (N) :
            if tmp[j] == 1 and i <= j:
                union(i,j)

    scheduled = list(map(int, input().split())) ## 여행 계획

    common = find(scheduled[0]-1)
    for place in scheduled :
        p = find(place-1)
        if p != common :
            print("NO")
            sys.exit()
    print("YES")
