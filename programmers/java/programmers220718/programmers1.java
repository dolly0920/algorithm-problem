package programmers.java.programmers220718;

import java.util.*;

public class programmers1 {

    class Solution {
        public int solution(int[][] board, int[] moves) {
            int answer = 0;

            Deque<Integer> deque = new ArrayDeque<>();

            for (int move : moves) {
                int extracted = pull(board, move-1);
                if (extracted == -1) {
                    continue;
                }
                if (deque.size() == 0) {
                    deque.add(extracted);
                    continue;
                }
                if (deque.getLast() == extracted) {
                    deque.removeLast();
                    answer += 2;
                    continue;
                }
                deque.add(extracted);
            }

            return answer;
        }

        private int pull(int[][] board, int line) {
            int extracted = -1; // 인형

            int index = 0;
            int length = board.length;

            while (index < length) {
                if (board[index][line] != 0) {
                    extracted = board[index][line];
                    board[index][line] = 0; // 제거
                    break;
                }
                index++;
            }
            return extracted;
        }
    }
}
