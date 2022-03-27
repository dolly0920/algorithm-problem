package baekjoon;

import java.util.Scanner;

/**
 * @author dolly0920
 * @github https://github.com/dolly0920
 * @since 2022-03-27
 */
public class boj1068 {

    static int nodeCount;
    static int[] parent;
    static int[] nodeStatus;
    static int root;
    static int deleteNode;
    static int leafCount = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        nodeCount = sc.nextInt(); // node 갯수
        parent = new int[nodeCount];
        nodeStatus = new int[nodeCount];
        for (int i = 0; i < nodeCount; i++) { // 0 ~ n-1 노드
            parent[i] = sc.nextInt();
            nodeStatus[i] = 1; // active
            if (parent[i] == -1) {
                root = i;
            }
        }
        deleteNode = sc.nextInt(); // 삭제할 node

        for (int i = 0; i < nodeCount; i++) { // 삭제된 노드의 하위 노드들 inactive
            if (findParent(i) == deleteNode) {
                nodeStatus[i] = -1; // inactive
            }
        }

        dfs(root);
        System.out.println(leafCount);
    }

    private static int findParent(int node) {
        if (node == root) {
            return node;
        }
        if (node == deleteNode) {
            return node;
        }
        return findParent(parent[node]);
    }

    private static void dfs(int node) {
        boolean isLeaf = true;
        for (int i = 0; i < nodeCount; i++) {
            if (parent[i] == node && nodeStatus[i] == 1) {
                dfs(i);
                isLeaf = false; // 자식 노드가 있으므로 leaf노드가 아니다.
            }
        }
        if (isLeaf && nodeStatus[node] == 1) { // 반례 케이스를 위해서 삭제되지 않은 노드라는 조건을 추가함
            leafCount++;
        }
    }
}
