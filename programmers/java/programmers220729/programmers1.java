package programmers.java.programmers220729;

import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/42626
public class programmers1 {
    class Solution {
        public int solution(int[] scoville, int K) {
            int answer = -1;

            PriorityQueue<Integer> minHeap = new PriorityQueue<>();

            for (int input : scoville) {
                minHeap.add(input);
            }

            if (minHeap.peek() >= K) {
                return 0;
            }

            int count = 0;

            while (minHeap.size() >= 2) {
                int firstLowestSpicy = minHeap.poll();
                int secondLowestSpicy = minHeap.poll();
                int mixed = firstLowestSpicy + (secondLowestSpicy*2);
                minHeap.add(mixed);
                count++;
                if (minHeap.peek() >= K) {
                    return count;
                }
            }

            return answer;
        }
    }
}
