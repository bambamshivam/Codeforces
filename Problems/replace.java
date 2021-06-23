import java.util.*;
public class replace{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		for(int i=0;i<a;i++){
			int a1=sc.nextInt();
			int d1=sc.nextInt();
			int ar1[]=new int[a1];
			for(int j=0;j<a1;j++){
				ar1[j]=sc.nextInt();
			}
			boolean flag=true;
			int min1=101, min2=101;
			for(int j=0;j<a1;j++){
				if(ar1[j]>d1)
					flag=false;
				if(ar1[j]<min1){
					min2=min1;
					min1=ar1[j];
				}
				else if(ar1[j]>=min1 && ar1[j]<min2)
					min2=ar1[j];
			}
			if(flag==true || min1+min2<=d1)
				System.out.println("YES");
			else
				System.out.println("NO");
		}
	}	
}