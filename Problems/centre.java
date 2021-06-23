import java.util.*;
class centre{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		centre obj=new centre();
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			int q=sc.nextInt();
			ArrayList<Integer> adjt[]=new ArrayList[n];
			for(int i=0;i<n;i++){
				adjt[i]=new ArrayList<Integer>();
			}
			for(int i=0;i<n-1;i++){
				int a=sc.nextInt();
				int b=sc.nextInt();
				adjt[a-1].add(b-1);
				adjt[b-1].add(a-1);
			}
			for(int i=0;i<q;i++){
				int k=sc.nextInt();
				int ar[]=new int[n];
				int fn=0;
				for(int j=0;j<k;j++){
					int p=sc.nextInt();
					if(j==0)
						fn=p-1;
					ar[p-1]=1;
				}
				for(int m=0;m<adjt.length;m++){
			    	for(int l=0;l<adjt[m].size();l++){
			    		System.out.print(adjt[m].get(l)+" ");
			    	}
			    	System.out.println();
			    }
				obj.lpl(ar,adjt,fn);
			}
		}
	}

	int[] bfs(int[] ar,ArrayList<Integer>[] adj,int fn){
		int[] dis = new int[ar.length];
		int[] b = new int[ar.length];
        Arrays.fill(dis, -1);
        Queue<Integer> q = new LinkedList<>();
        q.add(fn);
        dis[fn]=0;
        b[fn]=fn;
        while (!q.isEmpty()) {
            int t = q.poll();
            for(int i = 0; i < adj[t].size(); i++) {
            	if(ar[t]==1){
	                int v = adj[t].get(i);
	                if(ar[v]==1){
		                if(dis[t]+1>dis[v]) {
		                    q.add(v);
		                    dis[v] = dis[t] + 1;
		                    b[v]=t;
		                }
		            }
	            }
            }
        }
        int maxDis = 0;
        int nodeIdx = 0;
        for(int i = 0; i < ar.length; ++i) {
            if(dis[i] > maxDis) {
                maxDis = dis[i];
                nodeIdx = i;
            }
        }
        int b1[]=new int[b.length+1];
        b1[b.length]=nodeIdx;
        for(int i=0;i<b.length;i++){
        	b1[i]=b[i];
        }
        for(int m=0;m<b1.length;m++){
        	System.out.print(b1[m]+" ");
        }
        System.out.println();
        return b1;
	}

	void lpl(int[] ar,ArrayList<Integer>[] adj,int fn) {
        int t1[] = bfs(ar,adj,fn);
        int n1=t1[t1.length-1];
        int t2[] = bfs(ar,adj,n1);
        int b[]=new int[t2.length-1];
        for(int k=0;k<t2.length-1;k++){
        	b[k]=t2[k];
        }
        int n2=t2[t2.length-1];
        int n3=t2[t2.length-1];
        int c=0;
        while(b[n2]!=n1){
        	n2=b[n2];
        	c++;
        }
        c++;
        int c1=0;
        while(c1!=c/2){
    		n3=b[n3];
    		c1++;
    	}
        if(c%2==1){
        	System.out.println("1 "+(b[n3]+1));
        }
        else{
        	if(n3>b[n3])
        		System.out.println("2 "+b[n3]+1+" "+n3+1);
        	else
        		System.out.println("2 "+n3+1+" "+b[n3]+1);
        }
    }
}