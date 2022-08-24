package programmers.java.programmers220824;

// https://school.programmers.co.kr/learn/courses/30/lessons/118666
public class programmers1 {

    class Solution {
        public String solution(String[] survey, int[] choices) {
            String answer = "";

            String[] types = {"RT", "CF", "JM", "AN"};

            int[] scores = new int['Z'-'A'+1];

            for (int i = 0; i < choices.length; i++) {
                char a = survey[i].charAt(0);
                char b = survey[i].charAt(1);

                int score = choices[i] - 4;

                if (score == 0) continue;
                if (score > 0) scores[b - 'A'] += score;
                else scores[a - 'A'] -= score;
            }


            for (int i = 0; i < 4; i++) {
                char a = types[i].charAt(0);
                char b = types[i].charAt(1);

                int a_score = scores[a - 'A'];
                int b_score = scores[b - 'A'];

                if (a_score >= b_score) {
                    answer += a;
                } else {
                    answer += b;
                }
            }


            return answer;
        }
    }
}
