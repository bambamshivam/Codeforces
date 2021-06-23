import java.util.*;
public class paint1{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int ar[]=new int[n];
		for(int i=0;i<n;i++)
			ar[i]=sc.nextInt();
		int a=0;
		int b=0;
		int c=0;
		for(int i=0;i<n;i++){
			if(ar[i]!=a && ar[i]!=b){
				if(i+1<n && ar[i+1]==b)
					b=ar[i];
				else
					a=ar[i]; 
				c++;
			}
			else if(a!=ar[i]){
				a=ar[i];
				c++;
			}
			else if(b!=ar[i]){
				b=ar[i];
				c++;
			}
		}
		System.out.println(c);
	}
}