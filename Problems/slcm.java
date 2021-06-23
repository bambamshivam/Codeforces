import java.util.*;
public class slcm{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		slcm obj=new slcm();
		for(int i=0;i<a;i++){
			String s1=sc.next();
			String s2=sc.next();
			int lcm=s1.length()*s2.length()/obj.gcd(s1.length(),s2.length());
			String s1n="";
			String s2n="";
			for(int p=0;p<lcm/s1.length();p++)
				s1n+=s1;
			for(int p=0;p<lcm/s2.length();p++)
				s2n+=s2;
			if(s1n.equals(s2n))
				System.out.println(s1n);
			else
				System.out.println(-1);
		}
	}

	public int gcd(int a, int b){
		if(b==0)
			return a;
		else return gcd(b,a%b);
	}
}