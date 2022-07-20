package codility.java;

import java.util.*;

// https://app.codility.com/c/run/trainingSW8JN6-RXF/
public class BinaryGap {
    class Solution {
        public int solution(int N) {
            // write your code in Java SE 8
            List<Integer> converted = convert(N);

            int answer = 0;
            int index = 0;

            for (int i = 1; i < converted.size(); i++) {
                if (converted.get(i) == 1) {
                    answer = Math.max(answer, i - index - 1);
                    index = i;
                }
            }
            return answer;
        }

        private List<Integer> convert(int num) {
            List<Integer> answer = new ArrayList<>();
            Stack<Integer> stack = new Stack<>();

            while (num/2 > 0) {
                stack.push(num%2);
                num /= 2;
            }

            if (num % 2 == 1) {
                answer.add(1);
            }

            while (!stack.isEmpty()) {
                answer.add(stack.pop());
            }

            return answer;
        }
    }
}
