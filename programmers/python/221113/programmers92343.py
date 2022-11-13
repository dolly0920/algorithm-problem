## 구글링
def solution(info, edges):
    answer = set()
    visited = [0] * len(info)

    def DFS(sheep, wolf) :
        if sheep > wolf :
            answer.add(sheep)
        else :
            return

        for p, c in edges : ## 부모, 자식 노드의 관점에서
            if visited[p] == 1 and visited[c] == 0 : ## 부모 노드에는 방문했지만 자식 노드에는 방문하지 않은 케이스
                visited[c] = 1 ## 방문 체크
                if info[c] == 0 : ## 양인 경우
                    DFS(sheep+1, wolf)
                else : ## 늑대인 경우
                    DFS(sheep, wolf+1)
                visited[c] = 0 ## 방문 해제
    visited[0] = 1 ## 루트 노드 방문 체크
    DFS(1, 0) ## 루트 노드는 항상 양이다.

    return max(answer)

if __name__ == "__main__" :
    info = [0,0,1,1,1,0,1,0,1,0,1,1]
    edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
    print(solution(info, edges))