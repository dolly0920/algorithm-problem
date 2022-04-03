package baekjoon;

import java.util.Scanner;

public class boj1019 {
    /**
     * @author dolly0920
     * @github https://github.com/dolly0920
     * @since 2022-03-22
     */
    static int[] numberCount = new int[10];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        int start = 1;
        int point = 1;

        while (start <= n) {
            // 숫자를 **0 ~ **9 형태로 맞추는 과정
            while (n%10 != 9 && start <= n) {
                count(n, numberCount, point);
                n--;
            }
            while (start%10 != 0 && start <= n) {
                count(start, numberCount, point);
                start++;
            }
            if (start > n)
                break;
            //
            start /= 10;
            n /= 10;
            for (int i = 0; i < 10; i++) {
                numberCount[i] += (n-start+1)*point;
            }
            point *= 10;
        }

        for (int i=0; i<10; i++) {
            System.out.print(numberCount[i] + " ");
        }
    }

    private static void count(int x, int[] numberCount, int point) {
        while (x > 0) {
            numberCount[x%10] += point;
            x /= 10;
        }
    }
}
