import sys

sys.stdin = open("input.txt", "rt")

def findParent(x) :
    if parent[x] == x :
        return x
    parent[x] = findParent(parent[x])
    return parent[x]

def union(a, b) :
    root1 = findParent(a)
    root2 = findParent(b)

    if root1 != root2 :
        if rank[root1] > rank[root2] :
            parent[root2] = root1
        else :
            parent[root1] = root2
            if rank[root1] == rank[root2] :
                rank[root2] += 1

def check(a, b) :
    root1 = findParent(a)
    root2 = findParent(b)

    if root1 == root2 :
        return "YES"
    else :
        return "NO"

if __name__ == "__main__" :
    n, m = map(int, input().split())
    parent = [i for i in range (n+1)]
    rank = [0 for _ in range (n+1)]
    for _ in range (m) :
        command, a, b = map(int, input().split())
        if command == 0 :
            union(a, b)
        else :
            print(check(a, b))