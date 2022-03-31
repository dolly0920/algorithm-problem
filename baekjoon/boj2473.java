package baekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class boj2473 {

    static long[] acidity; // int, long 주의할 것!
    static long answer1, answer2, answer3;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 용액의 갯수
        acidity = new long[n];
        for (int i = 0; i < n; i++) {
            acidity[i] = sc.nextInt();
        }
        Arrays.sort(acidity);

        long sum = Long.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                long valueOfSum = acidity[i] + acidity[left] + acidity[right];
                long absoluteValue = Math.abs(valueOfSum);

                if (absoluteValue < sum) {
                    sum = absoluteValue;
                    answer1 = acidity[i];
                    answer2 = acidity[left];
                    answer3 = acidity[right];
                }

                if (valueOfSum > 0) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        System.out.println(answer1 + " " + answer2 + " " + answer3);
    }
}
