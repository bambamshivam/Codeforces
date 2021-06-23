import java.util.*;
public class snav{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int z=sc.nextInt();
		while(z-->0){
			int px=sc.nextInt();
			int py=sc.nextInt();
			String s=sc.next();
			int x=0;
			int y=0;
			for(int i=0;i<s.length();i++){
				if(s.charAt(i)=='R')
					x+=1;
				else if(s.charAt(i)=='L')
					x-=1;
				else if(s.charAt(i)=='U')
					y+=1;
				else if(s.charAt(i)=='D')
					y-=1;
			}
			if(x==px && y==py)
				System.out.println("YES");
			else{
				boolean flag=false;
				int a=px-x;
				int b=py-y;
				if(a>=0 && count(s,'L')>=a && b>=0 && count(s,'D')>=b)
					flag=true;
				if(a>=0 && count(s,'L')>=a && b<=0 && count(s,'U')>=y-py)
					flag=true;
				if(a<=0 && count(s,'R')>=x-px && b>=0 && count(s,'D')>=b)
					flag=true;
				if(a<=0 && count(s,'R')>=x-px && b<=0 && count(s,'U')>=y-py)
					flag=true;
				if(flag==true)
					System.out.println("YES");
				else
					System.out.println("NO");
			}
		}
	}

	public static int count(String str, char ch){
		int c=0;
		for(int i=0;i<str.length();i++){
			if(str.charAt(i)==ch)
				c+=1;
		}
		return c;
	}
}