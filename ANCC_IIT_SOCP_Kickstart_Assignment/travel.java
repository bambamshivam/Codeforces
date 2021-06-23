import java.util.*;
public class travel{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			ArrayList<ArrayList<Integer>>[] adj=new ArrayList[n];
			for(int i=0;i<n;i++){
				adj[i]=new ArrayList<ArrayList<Integer>>();

			}
			for(int i=0;i<n-1;i++){
				int a=sc.nextInt();
				int b=sc.nextInt();
				int c=sc.nextInt();
				ArrayList<Integer> a1=new ArrayList();
				a1.add(a-1);
				a1.add(c);
				adj[b-1].add(a1);
				ArrayList<Integer> b1=new ArrayList();
				b1.add(b-1);
				b1.add(c);
				adj[a-1].add(b1);
			}
			int v[]=new int[n];
			for(int i=0;i<n;i++){
				v[i]=0;
			}
			int b[]=new int[v.length];
	        int c[]=new int[v.length];
	        long d[]=new long[v.length];
	        for(int i=0;i<b.length;i++){
	        	b[i]=0;
	        	c[i]=0;
	        	d[i]=0;
	        }
			System.out.println(bfs(0,adj,v,b,c,d));
		}
	}

	static long bfs(int i,ArrayList<ArrayList<Integer>>[] adj,int v[],int b[],int c[],long d[]){
		LinkedList<Integer> queue = new LinkedList<Integer>();
        v[i]=1;
        
        queue.add(i);
        long min=(long)(Math.pow(10,18));
 
        while (queue.size() != 0)
        {
            i = queue.poll();
            if(i!=0 && adj[i].size()==1){
            	if(d[i]<min){
            		min=d[i];
            	}
            }
            for(int j=0;j<adj[i].size();j++)
            {
                int n = adj[i].get(j).get(0);
                if (v[n]==0)
                {
                    v[n] = 1;
                    b[n]=i;
                    c[n]=c[b[n]]+adj[i].get(j).get(1);
                    d[n]=d[b[n]]+c[n];
                    if(d[n]<min){
                    	queue.add(n);
                    }
                }
            }
        }
        return min;
	}
}