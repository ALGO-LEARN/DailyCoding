// 코드를 읽기전 정돈되지 않은 코드라 죄송합니다.

import java.util.*;
import java.io.*;

class prob{
	static int ans=0; // 마지막 출력값
	static int N;
	static int[][] arr; //좌석배치도
	static int[] seq; // 자리를 배정할 순서 sequence 배열
	static boolean[] isPushed; // 자리를 배정 받았는지 확인하는 isPushed 배열
	static int[] dy = {-1,0,0,1}; // delta y 
	static int[] dx = {0,-1,1,0}; // delta x 행과 열의 우선순위를 위해서 북, 서, 동 , 남 순으로 배치
	static ArrayList<ArrayList<Integer>> tree; // 호감도에 대한 정보를 위한 2중 ArrayList
	static void solve() throws IOException{
		//초기화
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		N=Integer.parseInt(br.readLine());
		arr=new int[N+1][N+1];
		seq=new int[N*N+1];
		isPushed=new boolean[N*N+1];
		tree=new ArrayList<>();
		for(int i=0; i<=N*N; i++)
			tree.add(new ArrayList<Integer>());
		
		for(int i=1; i<=N*N; i++) {
			st=new StringTokenizer(br.readLine());
			int num=Integer.parseInt(st.nextToken()); // 5개의 값 중 첫번째 값
			seq[i]=num;
			for(int j=0; j<4; j++) {
				int favorite=Integer.parseInt(st.nextToken()); // 호감있는 친구들에 대한 값
				tree.get(num).add(favorite); // num 번째있는 ArrayList 에 호감있는 친구들 추가.
			}
		}

		
		for(int num=1; num<=N*N; num++) {
			int next=seq[num]; //배치를 받을 학생
			int blnknum;  // 현재 위치를 기준으로 빈 공간을 카운트할 변수
			int blnkmaxnum=0; // 지난 위치 중 빈 공간이 가장 큰 위치를 기억하기 위해 사용할 카운트 변수
			int favnum; // 현재 위치를 기준으로 주변에 호감있는 친구를 카운트할 변수
			int favmaxnum = 0; //지난 위치 중 호감있는 친구의 수를 카운트할 변수
			int thereblnk=0; // 주변에 빈공간을 카운트할 변수 blnknum는 0으로 반복해서 초기화되지만 thereblnk는 그렇지 않을 예정.
			int bx=0,by=0;//주변에 빈 공간이 가장 많은 좌표를 기억할 변수
			int fx=0,fy=0; //주변에 호감있는 친구가 가장 많은 좌표를 기억할 변수
			int ny=0,nx=0; //상하좌우로 움직인 좌표를 위한 변수
			int f1 =tree.get(next).get(0); //호감있는 친구 1~4
			int f2 =tree.get(next).get(1);
			int f3 =tree.get(next).get(2);
			int f4 =tree.get(next).get(3);
			
			for(int i=1; i<=N; i++) 
			{
				for(int j=1; j<=N; j++) 
				{
					if(arr[i][j]!=0)
						continue;
					
					blnknum=0;
					favnum=0;
					
					for(int k=0; k<4; k++) //북,서,동,남 순서로 빈 공간과, 친구를 계산
					{
						ny=i+dy[k];
						nx=j+dx[k];
						
						if(nx<1 || nx>N || ny<1 || ny>N)
							continue;
						
						if(arr[ny][nx]==0)
							blnknum++;
						
						if(arr[ny][nx] == f1 || arr[ny][nx] == f2 || arr[ny][nx] == f3 || arr[ny][nx] == f4)
							favnum++;
						
					}
					
					//주변에 가장 많은 친구가 있는 위치를 위해
					if(favmaxnum<favnum && arr[i][j]==0) 
					{
						thereblnk=blnknum;
						favmaxnum=favnum;
						fy=i;
						fx=j;
					}
					
					//주변에 친구가 같은데 빈 공간은 더 많은 경우
					if(favmaxnum<=favnum && thereblnk<blnknum && arr[i][j]==0) 
					{
						favmaxnum=favnum;
						thereblnk=blnknum;
						fy=i;
						fx=j;
					}
					
					//주변에 가장 많은 빈 공간을 위해
					if(blnkmaxnum<blnknum && arr[i][j]==0) 
					{
						blnkmaxnum=blnknum;
						by=i;
						bx=j;
					}

				}
			}
			
			//주변 친구가 가장 많고, 주변 빈 공간도 더 많고, 배정받지 않았을 경우
			if(favmaxnum!=0 && !isPushed[next]) 
			{
				arr[fy][fx]=next;
				isPushed[next]=true;
			}
			
			//주변에 빈 공간이 가장 많은 경우, 하지만 친구는 없는 경우
			else if (blnkmaxnum!=0 && !isPushed[next]) 
			{
				arr[by][bx]=next;
				isPushed[next]=true;
			}			
			
			//주변 빈 공간도 없고, 친구도 없을 경우, 이 경우에는 행은 가장 적고 열이 그 다음으로 적은 빈 공간에 자리 배정
			else if(blnkmaxnum==0 && favmaxnum==0 && !isPushed[next]) 
			{
				boolean flag=false;
				for(int row=1; row<=N; row++) 
				{
					for(int col=1; col<=N; col++)
						if(arr[row][col]==0) 
						{
							arr[row][col]=next;
							isPushed[next]=true;
							flag=true;
							break;
						}
					if(flag)
						break;
				}
			}
			
		}
		

		//호감도 계산
		for(int i=1; i<=N; i++) {
			
			for(int j=1; j<=N; j++) {
				int favnum=0;
				int now = arr[i][j];
				int f1 =tree.get(now).get(0);
				int f2 =tree.get(now).get(1);
				int f3 =tree.get(now).get(2);
				int f4 =tree.get(now).get(3);
				for(int k=0; k<4; k++) {
					int ny=i+dy[k];
					int nx=j+dx[k];
					
					if(nx<1 || nx>N || ny<1 || ny>N)
						continue;
					
					if(arr[ny][nx] == f1 || arr[ny][nx] == f2 || arr[ny][nx] == f3 || arr[ny][nx] == f4)
						favnum++;
					}
				if(favnum==0)
					ans+=0;
				else if(favnum==1)
					ans+=1;
				else if(favnum==2)
					ans+=10;
				else if(favnum==3)
					ans+=100;
				else 
					ans+=1000;
				}

	}
		System.out.print(ans);
	}
		
}
public class Main {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		prob.solve();
	}

}

//22.03.19 
// 1. 친구를 배치할 수 있는 곳은 동서남북, 그리고 그 중 우선순위는 북 서 동 남 순임.
// 2-1. 좋아하는 학생이 인접한 칸 중 많은 칸
// 2-2. 2-1번칸이 많으면 빈칸이 가장 많은 칸
// 2-3. 2-2번칸이 많으면 행의 번호작은거 번저 열의 번호 나중 그래서 북 서 동 남
// 3. 저 3가지를 제어문을 통과해서 걸러내는 과정을 반복했는데, 아무리 생각해도 방법이 떠오르지 않아 닥치는대로 구현함

// 우선순위큐를 이용해서 2-1, 2-2, 2-3 을 구별하는 방법이 있었다.
// 보자마자 떠오르는 문제는 아니였고, 그만큼 시간이 오래 걸리는 문제
// 일단 구현부분에 대한 감이 제대로 잡혀있지 않음.
// 
