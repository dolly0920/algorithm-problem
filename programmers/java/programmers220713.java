package programmers.java;

import java.util.*;

public class programmers220713 {

    class Solution {
        public int[] solution(String[] id_list, String[] report, int k) {
            int[] answer = new int[id_list.length];

            Map<String, Integer> indexMap = new HashMap<>(); // <이름, 인덱스>
            Map<String, HashSet<String>> reportedMap = new HashMap<>(); // <신고당한 사람, 신고한 사람들>

            // 이름 한바퀴 순회 및 인덱스 저장 및 초기화
            for (int i = 0; i < id_list.length; i++) {
                reportedMap.put(id_list[i], new HashSet<>());
                indexMap.put(id_list[i], i);
            }

            // from, to
            for (int i = 0; i < report.length; i++) {
                String[] tmp = report[i].split(" ");
                String from = tmp[0];
                String to = tmp[1];
                reportedMap.get(to).add(from);
            }

            for (int i = 0; i < id_list.length; i++) {
                HashSet<String> reporters = reportedMap.get(id_list[i]);
                if (reporters.size() >= k) {
                    for (String reporter : reporters) {
                        answer[indexMap.get(reporter)]++;
                    }
                }
            }
            return answer;
        }
    }
}
