import java.util.*;
public class nezzar{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int b=sc.nextInt();
			int ar[]=new int[b];
			int i=0;
			while(b-->0){
				ar[i]=sc.nextInt();
				i++;
			}
			int c=0;
			int p=1;
			int n=ar[0];
			for(int j=0;j<ar.length;j++){
				if(ar[j]==n){
					c++;
				}
				else{
					p=Math.max(p,c);
					n=ar[j];
					c=1;
				}
			}
			p=Math.max(p,c);
			System.out.println(p);
		}
	}
}