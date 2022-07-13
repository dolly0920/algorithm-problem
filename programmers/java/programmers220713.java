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

    // solution 2 (다른 사람 풀이)
    class Solution2 {
        public int[] solution(String[] id_list, String[] report, int k) {
            int[] answer = new int[id_list.length];
            ArrayList<User> users = new ArrayList<>();
            HashMap<String,Integer> suspendedList = new HashMap<>(); //<이름>
            HashMap<String,Integer> idIdx = new HashMap<String,Integer>(); // <이름, 해당 이름의 User 클래스 idx>
            int idx = 0;

            for(String name : id_list) {
                idIdx.put(name,idx++);
                users.add(new User(name));
            }

            for(String re : report){
                String[] str = re.split(" ");
                //suspendedCount.put(str[0], suspendedCount.getOrDefault(str[0],0)+1);
                users.get( idIdx.get(str[0])).reportList.add(str[1]);
                users.get( idIdx.get(str[1])).reportedList.add(str[0]);
            }

            for(User user : users){
                if(user.reportedList.size() >= k)
                    suspendedList.put(user.name,1);
            }

            for(User user : users){
                for(String nameReport : user.reportList){
                    if(suspendedList.get(nameReport) != null){
                        answer[idIdx.get(user.name)]++;
                    }

                }
            }




            return answer;
        }
    }

    class User{
        String name;
        HashSet<String> reportList;
        HashSet<String> reportedList;
        public User(String name){
            this.name = name;
            reportList = new HashSet<>();
            reportedList = new HashSet<>();
        }
    }
}
