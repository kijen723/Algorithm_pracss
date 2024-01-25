package com.algorithm.practice.boj;

import java.io.FileInputStream;
import java.util.Scanner;

/*
BOJ 1592 영식이와 친구들
 */
public class Solution1592 {
    static int N, M, L;

    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        L = sc.nextInt() % N;

        int[] ballCount = new int[N];
        int idx = 0, answer = 0;

        while (true) {
            ballCount[idx]++;
            answer++;

            if (ballCount[idx] == M) {
                break;
            }

            idx = pass(idx, ballCount[idx] % 2);
        }

        System.out.println(answer - 1);

        sc.close();
    }

    static int pass(int idx, int dir) {
        if (dir == 0) {
            if (idx - L < 0) {
                idx = N + idx - L;
            } else {
                idx = idx - L;
            }
        } else {
            if (idx + L >= N) {
                idx = idx + L - N;
            } else {
                idx = idx + L;
            }
        }

        return idx;
    }
}
