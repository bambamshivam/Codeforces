import java.util.*;
public class strange{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		strange obj=new strange();
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			int ar[]=new int[n];
			for(int i=0;i<n;i++){
				ar[i]=sc.nextInt();
			}
			int c=0;
			int d=0;
			int min=Integer.MAX_VALUE;
			ArrayList<Integer> neg=new ArrayList<Integer>();
			for(int i=0;i<n;i++){
				if(ar[i]<=0){
					c++;
					neg.add(ar[i]);
				}
				if(ar[i]==0)
					d++;
				if(ar[i]>0 && ar[i]<min)
					min=ar[i];
			}
			int m=0;
			Collections.sort(neg);
			for(int i=0;i<neg.size()-1;i++){
				if(Math.abs(neg.get(i)-neg.get(i+1))<min){
					m=1;
					break;
				}
			}
			if(c==ar.length)
				System.out.println(c);
			else if(d>1)
				System.out.println(c);
			else if(m==1)
				System.out.println(c);
			else
				System.out.println(c+1);
		}
	}

	
}