import java.util.*;
public class cubes{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			long n=sc.nextLong();
			long y=1;
			long x=(long)Math.pow(n,1.0*1/3);
			x+=2;
			int p=0;
			for(long i=1;i<x;i++){
				long k=(long)Math.round(Math.pow(n - i*i*i,1.0*1/3));
				if(n - i*i*i>0 && k*k*k+ i*i*i ==n){
					System.out.println("YES");
					p=1;
					break;
				}
			}
			if(p==0)
				System.out.println("NO");
		}
	}
}