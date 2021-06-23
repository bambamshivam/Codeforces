import java.util.*;
public class brem{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			int n=sc.nextInt();
			int ar[]=new int[n];
			for(int i=0;i<n;i++)
				ar[i]=sc.nextInt();
			int c0=0;
			int c2=0;
			int c1=0;
			int c=0;
			for(int i=0;i<n;i++){
				if(ar[i]%3==0)
					c0++;
				if(ar[i]%3==1)
					c1++;
				if(ar[i]%3==2)
					c2++;
			}
			if(c0>(n/3)){
				int m=c0-(n/3);
				if((n/3)-c1 > 0){
					if(m>(n/3)-c1){
						c+=(n/3 -c1);
						c+=2*(n/3 -c2);
					}
					else
						c+=m + 2*(c2- n/3);
				}
				else
					c+=2*(c0 - (n/3)) + (c1- (n/3));
			}
			else if(c1>(n/3)){
				int m=c1-(n/3);
				if((n/3)-c2 > 0){
					if(m>(n/3)-c2){
						c+=(n/3 -c2);
						c+=2*(n/3 -c0);
					}
					else
						c+=m + 2*(c0- n/3);
				}
				else
					c+=2*(c1 - (n/3)) + (c2- (n/3));
			}
			else{
				int m=c2-(n/3);
				if((n/3)-c0 > 0){
					if(m>(n/3)-c0){
						c+=(n/3 -c0);
						c+=2*(n/3 -c1);
					}
					else
						c+=m + 2*(c1- n/3);
				}
				else
					c+=2*(c2 - (n/3)) + (c0- (n/3));
			}
			System.out.println(c);
		}
	}
}