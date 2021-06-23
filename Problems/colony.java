import java.util.*;
public class colony{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int k=sc.nextInt();
			int ar[]=new int[n];
			for(int i=0;i<n;i++)
				ar[i]=sc.nextInt();
			int b=k;
			int h=0;
			while(b>0){
				h=0;
				boolean flag=false;
				while(h<n-1){
					if(ar[h]>=ar[h+1])
						h++;
					else{
						ar[h]+=1;
						break;
					}
				}
				if(h==n-1){
					break;
				}
				b--;
			}
			if(h==n-1)
				System.out.println(-1);
			else
				System.out.println(h+1);
		}
	}
}