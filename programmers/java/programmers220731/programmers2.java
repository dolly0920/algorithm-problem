package programmers.java.programmers220731;

import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/42746
public class programmers2 {
    class Solution {
        public String solution(int[] numbers) {
            String answer = "";

            List<String> arr = new ArrayList<>();

            for (int num : numbers) {
                arr.add(Integer.toString(num));
            }

            Collections.sort(arr, (a,b) -> {
                return (b+a).compareTo(a+b);
            });

            // 입력이 [0, 0, 0] case
            if (Integer.parseInt(arr.get(0)) == 0) {
                return "0";
            }

            for (String num : arr) {
                answer += num;
            }

            return answer;
        }
    }
}
