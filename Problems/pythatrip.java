import java.util.*;
public class pythatrip{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int i=3;
			int c=0;
			while((i*i + 1)/2 <=n){
				c++;
				i+=2;
			}
			System.out.println(c);
		}
	}
}