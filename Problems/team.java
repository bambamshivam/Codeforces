import java.util.*;
public class team{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int b=sc.nextInt();
		while(b-->0){
			int n=sc.nextInt();
			int k=sc.nextInt();
			int t[]=new int[n];
			int c=0;
			for(int i=0;i<n;i++){
				t[i]=sc.nextInt();
				if(t[i]>=k){
					t[i]=-1;
					c++;
				}
			}
			int tn[]=new int[n-c];
			int j=0;
			for(int i=0;i<n;i++){
				if(t[i]!=-1){
					tn[j]=t[i];
					j++;
				}
			}
			Arrays.sort(tn);
			int m=tn.length;
			int l=0;
			int r=m-1;
			while(r-l+1>1){
				boolean flag=false;
				for(int i=l+1;i<=r;i++){
					if(tn[l]+tn[i]>=k){
						int d=Math.min(r-i,i-1-l);
						c+=(d+1);
						if(d==r-i){
							r=i-1;
							l=l+d+1;
						}
						else{
							l=i+d+1;
						}
						flag=true;
						break;
					}
				}
				if(flag==false)
					l++;
			}
			System.out.println(c);
		}
	}
}