import java.util.*;
public class kl{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int q=sc.nextInt();
		int ar[]=new int[n];
		for(int i=0;i<n;i++)
			ar[i]=sc.nextInt();
		int c=0;
		for(int i=0;i<n;i++){
			if(ar[i]==1)
				c+=1;
		}
		while(q-->0){
			int t=sc.nextInt();
			int x=sc.nextInt();
			if(t==1){
				if(ar[x-1]==1)
					c-=1;
				else
					c+=1;
			}
			else{
				if(x<=c)
					System.out.println(1);
				else
					System.out.println(0);
			}
		}
	}
}