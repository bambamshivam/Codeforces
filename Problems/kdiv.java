import java.util.*;
public class kdiv{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int k=sc.nextInt();
			if(k>=n && k%n==0){
				System.out.println((k/n));
			}
			else if(k>n && k%n!=0){
				System.out.println((k/n)+1);
			}
			else{
				k=(int)Math.ceil((double)(n*10.0/(k*10.0)))*k;
				if(k%n==0)
				System.out.println((k/n));
				else
				System.out.println((k/n)+1);
			}
		}
	}
}