import java.util.*;
class cross{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int ar1[]=new int[n];
		int ar2[]=new int[n];
		for(int i=0;i<n;i++){
			ar1[i]=sc.nextInt();
		}
		for(int i=0;i<n;i++){
			if(i-1>=0){
				if(ar1[i-1]>=ar1[i]){
					if(ar2[i-1]==1)
						ar2[i-1]+=1;
					ar2[i]=1;
				}
				else{
					ar2[i]=ar2[i-1]+1;
				}
			}
			else{
				ar2[i]=1;
			}
		}
		int sum=0;
		for(int i=0;i<n;i++){
			sum+=ar2[i];
		}
		System.out.println(sum);
	}
}