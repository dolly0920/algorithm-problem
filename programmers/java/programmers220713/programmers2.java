package programmers.java.programmers220713;

// https://school.programmers.co.kr/learn/courses/30/lessons/86051
public class programmers2 {
    class Solution {
        public int solution(int[] numbers) {
            int answer = 45;
            for (int number : numbers) {
                answer -= number;
            }
            return answer;
        }
    }
}
