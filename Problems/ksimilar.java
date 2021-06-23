import java.util.*;
public class ksimilar{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int q=sc.nextInt();
		int k=sc.nextInt();
		int ar[]=new int[n];
		for(int i=0;i<n;i++)
			ar[i]=sc.nextInt();
		while(q-->0){
			int l=sc.nextInt();
			int r=sc.nextInt();
			int t=k-ar[r-1]+ar[l-1]-1+2*(ar[r-1]-ar[l-1]-1-(r-l-1));
			System.out.println(t);
		}
	}
}