import java.util.*;
public class makeodd{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int ar[]=new int[n];
			int t=-1;
			int c=0;
			for(int i=0;i<n;i++){
				ar[i]=sc.nextInt();
				if(ar[i]%2!=0)
					t=ar[i];
				else
					c++;
			}
			if(t==-1)
				System.out.println(-1);
			else
				System.out.println(c);
		}
	}
}