import java.util.*;
public class barr{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			int ar[]=new int[n];
			for(int i=0;i<n;i++){
				ar[i]=sc.nextInt();
			}
			int c=0;
			Arrays.sort(ar);
			while(c<ar.length && ar[c]==ar[0]){
				c++;
			}
			if(c==ar.length)
				System.out.println(0);
			else
				System.out.println(ar.length-c);
		}
	}
}