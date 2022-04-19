import java.util.*;
public class C_Make_it_Increasing{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        long n=sc.nextLong();
        long a[]=new long[(int) n];
        for(int i=0;i<n;i++) a[i]=sc.nextInt();
        long ans=10^18;
        for(int i=0;i<n;i++){
            long c=0, prev=0;
            for(int j=i-1;j>=0;j-=1){
                long cur=((prev/a[j])+1)*a[j];
                c+=(prev/a[j])+1;
                prev=cur;
            }
            prev=0;
            for(int j=i+1;j<n;j+=1){
                long cur=((prev/a[j])+1)*a[j];
                c+=(prev/a[j])+1;
                prev=cur;
            }
            ans=Math.min(ans,c);
        }
        sc.close();
        System.out.println(ans);
    }
}