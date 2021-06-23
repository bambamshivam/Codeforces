import java.util.*;
public class shift{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			long s=0;
			int p=0;
			int ar[]=new int[n];
			for(int i=0;i<n;i++){
				ar[i]=sc.nextInt();
				s+=ar[i];
				if(s<(i+1)*(i)/2)
					p=1;
			}
			if(p==1)
				System.out.println("NO");
			else
				System.out.println("YES");
		}
	}
}