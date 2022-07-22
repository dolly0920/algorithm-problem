package programmers.java.programmers220722;

import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/1835
public class programmers1 {
    class Solution {
        int answer = 0;
        boolean[] visited = new boolean[8];

        public int solution(int n, String[] data) {
            char[] input = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
            dfs(input, "", data);
            return answer;
        }

        private void dfs(char[] input, String str, String[] data) {
            if (str.length() == 8) {
                if (isPossible(str, data)) {
                    answer++;
                }
                return;
            }

            for (int i=0; i<8; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    dfs(input, str + input[i], data);
                    visited[i] = false;
                }
            }
        }

        private boolean isPossible(String str, String[] data) {
            for (String condition : data) {
                char first = condition.charAt(0);
                char second = condition.charAt(2);
                char c = condition.charAt(3);
                int distance = Character.getNumericValue(condition.charAt(4));

                int diff = Math.abs(str.indexOf(first)-str.indexOf(second))-1;

                if (c == '=' && diff != distance) return false;
                if (c == '>' && diff <= distance) return false;
                if (c == '<' && diff >= distance) return false;
            }
            return true;
        }
    }
}
