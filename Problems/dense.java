import java.util.*;
public class dense{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int ar[]=new int[n];
			for(int i=0;i<n;i++)
				ar[i]=sc.nextInt();
			int c=0;
			for(int i=0;i<n-1;i++){
				int max=Math.max(ar[i],ar[i+1]);
				int min=Math.min(ar[i],ar[i+1]);

				if(max*1.0/min > 2){

					double p=max*1.0/(2*min);
					double t=Math.log(p)/Math.log(2);
					c+=(int)Math.ceil(t);
				}
			}
			System.out.println(c);
		}
	}
}