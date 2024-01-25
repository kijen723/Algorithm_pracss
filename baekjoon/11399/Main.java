// baekjoon 11399 Java

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] P = new int[N];

        for (int i = 0; i < N; i++) {
            P[i] = sc.nextInt();
        }

        Arrays.sort(P);

        int answer = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i + 1; j++) {
                answer += P[j];
            }
        }

        System.out.println(answer);

        sc.close();
    }
}