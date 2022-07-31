package excercise;

import java.util.*;

public class PlayGround {

    public static void main(String[] args) {
        System.out.println("Hello World!");

        List<String> test = new ArrayList<>(Arrays.asList("c", "b", "a"));

        System.out.println(test);

        Collections.sort(test, (a, b) -> {
            return (a+b).compareTo(b+a); // compareTo : 입력값보다 크면 1, 같으면 0, 작으면 -1
        });

        System.out.println(test);
    }
}
