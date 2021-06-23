import java.util.*;
public class pattern{
	public static void main(String[] args) {
		pattern obj=new pattern();
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int m=sc.nextInt();
		int k=sc.nextInt();
		String pat[]=new String[n];
		for(int i=0;i<n;i++)
			pat[i]=sc.next();
		HashMap<String, String> hm=new HashMap<String, String>();
		strn a[]=new strn[m];
		for(int i=0;i<m;i++){
			String str=sc.next();
			int t=sc.nextInt();
			hm.put(pat[t-1],str);
			a[i]=new strn(str,t);
		}
		boolean flag=false;
		ArrayList<strn> ar=new ArrayList<strn>(); 
		for(int i=0;i<m;i++){
			if(obj.match(a[i].str,pat[a[i].p-1])==false){
				flag=true;
			}
			ar.add(new strn(pat[a[i].p-1],a[i].p));
			for(int j=0;j<i;j++){
				if(obj.match(a[i].str,ar.get(j).str)){
					if(obj.match(hm.get(ar.get(j).str),pat[a[i].p - 1])){
						flag=true;
						break;
					}
					else{
						strn s1=ar.get(j);
						ar.remove(j);
						ar.add(s1);					
					}
				}
				if(flag==true)
					break;
			}
			if(flag==true)
				break;
		}
		if(flag==true)
			System.out.println("NO");
		else{
			System.out.println("YES");
			int used[]=new int[n];
			for(int i=0;i<m;i++)
				used[i]=-1;
			for(int i=0;i<m;i++){
				used[ar.get(i).p-1]=1;
				System.out.print(ar.get(i).p+" ");
			}
			for(int i=0;i<m;i++){
				if(used[i]==-1)
					System.out.print(i+1 + " ");
			}
		}
	}

	static boolean match(String s, String patter){
		for(int i=0;i<patter.length();i++){
			if(patter.charAt(i)=='_')
				continue;
			else if(patter.charAt(i)!=s.charAt(i))
				return false;
		}
		return true;
	}

	public static class strn{
		int p;
		String str;
		strn(String str, int p){
			this.p=p;
			this.str=str;
		}
	}
}