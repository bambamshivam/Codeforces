import java.util.*;
public class inflation{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int k=sc.nextInt();
			long ar[]=new long[n];
			for(int i=0;i<n;i++){
				ar[i]=sc.nextLong();
			}
			double s=0.0;
			double c=0.0;
			for(int i=0;i<n-1;i++){
				s+=ar[i];
				double t=0.0;
				double r=ar[i+1]/s;
				if(r>k/100.0){
					t=(ar[i+1]*100.0/k)-s;
					c+=t;
				}
				s+=t;
			}
			if(c-(Math.floor(c))<0.001)
				c=Math.floor(c);
			else
				c=Math.ceil(c);
			System.out.println((long)c);
		}
	}
}