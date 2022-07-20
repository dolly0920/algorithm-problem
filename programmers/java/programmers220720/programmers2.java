package programmers.java.programmers220720;

import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/1829
public class programmers2 {
    class Solution {

        public class Pair {
            private int left;
            private int right;

            public Pair(int left, int right) {
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

        public int[] solution(int m, int n, int[][] picture) {
            int[][] visited = new int[m][n];
            initialize(m, n, visited);

            int numberOfArea = 0;
            int maxSizeOfOneArea = 0;

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (picture[i][j] != 0 && visited[i][j] == 0) {
                        visited[i][j] = 1;
                        maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(i, j, m, n, visited, picture));
                        numberOfArea++;
                    }
                }
            }

            int[] answer = new int[2];
            answer[0] = numberOfArea;
            answer[1] = maxSizeOfOneArea;
            return answer;
        }

        private void initialize(int m, int n, int[][] arr) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    arr[i][j] = 0;
                }
            }
        }

        private int bfs(int x, int y, int m, int n, int[][] visited, int[][] picture) {
            int[] dx = {1, -1, 0, 0};
            int[] dy = {0, 0, 1, -1};
            int count = 0;

            Queue<Pair> queue = new LinkedList<>();
            visited[x][y] = 1;
            queue.add(new Pair(x, y));

            while (!queue.isEmpty()) {
                Pair curr = queue.poll();
                int cur_x = curr.getLeft();
                int cur_y = curr.getRight();
                count++;

                for (int i = 0; i < 4; i++) {
                    int next_x = cur_x + dx[i];
                    int next_y = cur_y + dy[i];
                    if (checkBound(next_x, next_y, m, n)) {
                        if (visited[next_x][next_y] == 0 && picture[cur_x][cur_y] == picture[next_x][next_y]) {
                            visited[next_x][next_y] = 1;
                            queue.add(new Pair(next_x, next_y));
                        }
                    }
                }
            }

            return count;
        }

        private boolean checkBound(int x, int y, int m, int n) {
            return x >= 0 && y >= 0 && x < m && y < n;
        }
    }
}
