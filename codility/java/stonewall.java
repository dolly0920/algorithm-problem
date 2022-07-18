package codility.java;

import java.util.*;

public class stonewall {
    class Solution {
        public int solution(int[] H) {
            // write your code in Java SE 8
            int answer = 0;

            Stack<Integer> stack = new Stack<>();

            for (int height : H) {
                while (!stack.isEmpty()) {
                    if (stack.peek() > height) {
                        answer++;
                        stack.pop();
                    } else if (stack.peek() < height) {
                        stack.add(height);
                        break;
                    } else {
                        break;
                    }
                }
                if (stack.isEmpty()) {
                    stack.add(height);
                }
            }

            return answer + stack.size();
        }
    }
}
