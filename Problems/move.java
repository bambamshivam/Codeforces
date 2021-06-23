import java.util.*;
public class move{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int m=sc.nextInt();
		while(m-->0){
			int n=sc.nextInt();
			String str=sc.next();
			int a=0;
			while(n-->0){
				if(str.charAt(n)=='1')
					a+=90;
				else
					a-=90;
			}
			int t=a/360;
			a-=t*360;
			if(a==90 || a==-270)
				System.out.println("N");
			else if(a==180 || a==-180)
				System.out.println("W");
			else if(a==-90 || a==270)
				System.out.println("S");
			else
				System.out.println("E");
		}
	}
}