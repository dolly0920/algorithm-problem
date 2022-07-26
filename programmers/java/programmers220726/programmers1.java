package programmers.java.programmers220726;

import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/67256
public class programmers1 {
    class Pair {
        private int x;
        private int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }

    class Solution {
        private Map<Integer, Pair> indexMap = new HashMap<>();
        private Set<Integer> left_num = Set.of(1, 4, 7);
        private Set<Integer> right_num = Set.of(3, 6, 9);

        private Pair leftHand = new Pair(3, 0);
        private Pair rightHand = new Pair(3, 2);

        {
            indexMap.put(1, new Pair(0, 0));
            indexMap.put(2, new Pair(0, 1));
            indexMap.put(3, new Pair(0, 2));
            indexMap.put(4, new Pair(1, 0));
            indexMap.put(5, new Pair(1, 1));
            indexMap.put(6, new Pair(1, 2));
            indexMap.put(7, new Pair(2, 0));
            indexMap.put(8, new Pair(2, 1));
            indexMap.put(9, new Pair(2, 2));
            indexMap.put(0, new Pair(3, 1));
        }

        public String solution(int[] numbers, String hand) {
            String answer = "";

            for (int num : numbers) {
                if (left_num.contains(num)) {
                    leftHand = indexMap.get(num);
                    answer += "L";
                    continue;
                }
                if (right_num.contains(num)) {
                    rightHand = indexMap.get(num);
                    answer += "R";
                    continue;
                }
                answer += move(num, hand);
            }

            return answer;
        }

        private String move(int target, String hand) {
            Pair target_location = indexMap.get(target);

            int left_distance = distance(leftHand, target_location);
            int right_distance = distance(rightHand, target_location);

            if (left_distance > right_distance) {
                rightHand = target_location;
                return "R";
            }
            if (right_distance > left_distance) {
                leftHand = target_location;
                return "L";
            }

            if ("right".equals(hand)) {
                rightHand = target_location;
                return "R";
            } else {
                leftHand = target_location;
                return "L";
            }
        }

        private int distance(Pair a, Pair b) {
            return Math.abs(a.getX() - b.getX()) + Math.abs(a.getY() - b.getY());
        }
    }
}
