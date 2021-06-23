import java.util.*;
class comball{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			int m=sc.nextInt();
			int an[]=new int[1001];
			for(int i=0;i<n;i++){
				int a=sc.nextInt();
				an[a]++;
			}
			int am[]=new int[1001];
			for(int i=0;i<m;i++){
				int a=sc.nextInt();
				am[a]++;
			}
			int c=0;
			for(int i=0;i<=1000;i+=3){
				if(an[i]==1 && am[i]==1){
					System.out.print(i+" ");
					c++;
				}
			}
			if(c==0)
				System.out.print(-1);
			System.out.println();
		}
	}
}