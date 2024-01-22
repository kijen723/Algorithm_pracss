// swea 5215 Java

import java.util.Scanner;
// import java.io.FileInputStream;

class Solution
{
	static int N = 0, L = 0, answer = 0;
	static int[][] arr;
	
	public static void main(String args[]) throws Exception
	{
		// System.setIn(new FileInputStream("input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
	
		for(int test_case = 1; test_case <= T; test_case++)
		{
			N = sc.nextInt();
			L = sc.nextInt();
			arr = new int[N][2];
			
			for (int i = 0; i < arr.length; i++) {
				arr[i][0] = sc.nextInt();
				arr[i][1] = sc.nextInt();
			}
			
            answer = 0;
			dfs(0, 0, 0);
			
			System.out.printf("#%d %d\n", test_case, answer);
		}

        sc.close();
	}
	
	static void dfs(int n, int score, int cal) {
		if (cal > L) {
            
			return;
		}
		
		if (n == N) {
			if (answer < score) {
				answer = score;
			}
			
			return;
		}
		
		dfs(n + 1, score + arr[n][0], cal + arr[n][1]);
		dfs(n + 1, score, cal);		
	}
	
}
