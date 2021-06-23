import java.util.*;
public class flagstones{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		long m=sc.nextLong();
		long n=sc.nextLong();
		long a=sc.nextLong();
		long p=m/a;
		if(m%a!=0)
			p=p+1;
		long q=n/a;
		if(n%a!=0)
			q=q+1;
		System.out.println(p*q);
	}
}