import java.util.*;
public class arena{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int ar[]=new int[n];
			for(int i=0;i<n;i++)
				ar[i]=sc.nextInt();
			Arrays.sort(ar);
			int c=1;
			for(int i=1;i<n;i++){
				if(ar[i]!=ar[0])
					break;
				c++;
			}
			System.out.println(n-c);
		}
	}
}