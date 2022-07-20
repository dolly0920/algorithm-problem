package programmers.java.programmers220720;

import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/49189
public class programmers1 {
    class Solution {
        public class Pair {
            private int left;
            private int right;

            Pair(int left, int right) {
                this.left = left;
                this.right = right;
            }

            public int getLeft() {
                return left;
            }

            public int getRight() {
                return right;
            }
        }

        public int solution(int n, int[][] edge) {

            Map<Integer, Set<Integer>> pathMap = new HashMap<>();

            int[] visited = new int[n+1];

            initialize(n, visited);

            // 간선 체크
            for (int i = 0; i < edge.length; i++) {
                int left = edge[i][0];
                int right = edge[i][1];

                Set<Integer> path1 = pathMap.getOrDefault(left, new HashSet<>());
                Set<Integer> path2 = pathMap.getOrDefault(right, new HashSet<>());
                path1.add(right);
                path2.add(left);

                pathMap.put(left, path1);
                pathMap.put(right, path2);
            }

            // 가장 멀리 떨어진 노드와의 거리
            int start = 1;
            int longest = -1;
            Queue<Pair> queue = new LinkedList<>();
            visited[start] = 1;
            queue.add(new Pair(start, 0));

            Set<Integer> nodes = new HashSet<>();

            while (!queue.isEmpty()) {
                Pair current = queue.poll();
                int curNode = current.getLeft();
                int curValue = current.getRight();

                if (curValue != longest) {
                    longest = curValue; // 갱신
                    nodes = new HashSet<>();
                    nodes.add(curNode);
                } else {
                    nodes.add(curNode);
                }

                Set<Integer> nextNodes = pathMap.getOrDefault(curNode, new HashSet<>());
                for (Integer node : nextNodes) {
                    if (visited[node] == 1) {
                        continue;
                    }
                    visited[node] = 1;
                    queue.add(new Pair(node, curValue+1));
                }
            }
            return nodes.size();
        }

        private void initialize(int n, int[] arr) {
            for (int i = 0; i < n+1; i++) {
                arr[i] = 0;
            }
        }
    }
}
