package programmers.java.programmers220731;

// https://school.programmers.co.kr/learn/courses/30/lessons/49191
public class programmers1 {
    class Solution {
        public int solution(int n, int[][] results) {
            int answer = 0;

            int[][] players_info = new int[n+1][n+1]; // 1 : win, -1 : lose

            for (int i = 0; i < results.length; i++) {
                int winner = results[i][0];
                int loser = results[i][1];

                players_info[winner][loser] = 1;
                players_info[loser][winner] = -1;
            }

            // 플로이드-와샬
            for (int i = 1; i < n+1; i++) {
                for (int j = 1; j < n+1; j++) {
                    for (int k = 1; k < n+1; k++) {
                        if (players_info[i][k] == 1 && players_info[k][j] == 1) { // i > k, k > j => i > j
                            players_info[i][j] = 1;
                            players_info[j][i] = -1;
                        }
                        if (players_info[i][k] == -1 && players_info[k][j] == -1) { // i < k, k < j => i < j
                            players_info[i][j] = -1;
                            players_info[j][i] = 1;
                        }
                    }
                }
            }

            for (int i = 1; i < n+1; i++) {
                int count = 0;
                for (int j = 1; j < n+1; j++) {
                    if (players_info[i][j] != 0) {
                        count++;
                    }
                }
                if (count == n-1) {
                    answer++;
                }
            }

            return answer;
        }
    }
}
