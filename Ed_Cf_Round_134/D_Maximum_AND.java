import java.util.*;
public class D_Maximum_AND{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int tt=sc.nextInt();
        while(tt-->0){
            int n=sc.nextInt();
            ArrayList<Integer> s=new ArrayList<>();
            for(int i=0;i<n;i++)s.add(i);
            ArrayList<ArrayList<Integer>> l=new ArrayList<>();
            l.add(s);
            l.add(s);
            long ans=0;
            ArrayList<Integer> a=new ArrayList<>();
            ArrayList<Integer> b=new ArrayList<>();
            for(int i=0;i<n;i++)a.add(sc.nextInt());
            for(int i=0;i<n;i++)b.add(sc.nextInt());
            for(int j=30;j>=0;j--){
                int t=(1<<j);
                int c=0;
                ArrayList<ArrayList<Integer>> p=new ArrayList<>();
                for(int k=0;k<l.size()-1;k+=2){
                    ArrayList<Integer> s1=l.get(k);
                    ArrayList<Integer> s2=l.get(k+1);
                    ArrayList<Integer> s10=new ArrayList<>();
                    ArrayList<Integer> s11=new ArrayList<>();
                    ArrayList<Integer> s20=new ArrayList<>();
                    ArrayList<Integer> s21=new ArrayList<>();
                    for(int z=0;z<s1.size();z++){
                        if((t&(a.get(s1.get(z))))>0)s11.add(s1.get(z));
                        else s10.add(s1.get(z));
                    }
                    for(int z=0;z<s2.size();z++){
                        if((t&(b.get(s2.get(z))))>0)s21.add(s2.get(z));
                        else s20.add(s2.get(z));
                    }
                    if(s10.size()==s21.size()){
                        p.add(s10);p.add(s21);p.add(s11);p.add(s20);c+=2;
                    }
                }
                if(c==l.size()){
                    ans+=t;l=p;
                }
            }
            System.out.println(ans);
        }
        sc.close();
    }
}