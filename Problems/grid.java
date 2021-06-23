import java.util.*;
class grid{
	public static void main(String args[]){
		grid obj=new grid();
		Scanner sc=new Scanner(System.in);
		int m=sc.nextInt();
		int n=sc.nextInt();
		int s=sc.nextInt();
		int ar[][]=new int[m*n][9];
		int box[][]=new int[m][n];
		int c=0;
		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++){
				box[i][j]=c;
				c++;
			}
		}
		ArrayList<Integer>[] adj=new ArrayList[m*n];
		int dist[]=new int[m*n];
		int b[]=new int[m*n];
		for(int i=0;i<m*n;i++){
			dist[i]=Integer.MAX_VALUE;
			adj[i]=new ArrayList<Integer>();
			ar[i][0]=sc.nextInt();
			for(int j=1;j<9;j++){
				ar[i][j]=sc.nextInt();
				if(ar[i][j]==1){
					int a1=(int)Math.ceil((double)(i+1)/n);
					int a2=(i+1)-((a1-1)*n);
					int coord[]=obj.dir(j,a1,a2);
					adj[i].add(box[coord[0]-1][coord[1]-1]);
				}
			}
		}
		dist[s-1]=0;
		obj.path(s-1,dist,b,adj);
		obj.track(s-1,0,b);
		obj.track(s-1,n-1,b);
		obj.track(s-1,(m-1)*n ,b);
		obj.track(s-1,m*n -1,b);
	}

	void track(int src,int dest,int b[]){
		int k=dest;
		ArrayList<Integer> t=new ArrayList<Integer>();
		t.add(k);
		while(b[k]!=src){
			k=b[k];
			t.add(k);
		}
		t.add(src);
		for(int i=t.size()-1;i>=0;i--)
			System.out.print(t.get(i)+1+" ");
		System.out.println();
	}

	void path(int src,int dist[],int b[],ArrayList<Integer> adj[]){
		grid obj=new grid();
		for(int i=0;i<adj[src].size();i++){
			if(dist[adj[src].get(i)]>dist[src]+1){
				dist[adj[src].get(i)]=dist[src]+1;
				b[adj[src].get(i)]=src;
				obj.path(adj[src].get(i),dist,b,adj);
			}
		}
	}

	int[] dir(int i,int a,int b){
		int t[]=new int[2];
		switch(i){
			case 1:{
				a-=1;
				break;
			}
			case 2:{
				a-=1;
				b+=1;
				break;
			}
			case 3:{
				b+=1;
				break;
			}
			case 4:{
				a+=1;
				b+=1;
				break;
			}
			case 5:{
				a+=1;
				break;
			}
			case 6:{
				a+=1;
				b-=1;
				break;
			}
			case 7:{
				b-=1;
				break;
			}
			case 8:{
				a-=1;
				b-=1;
				break;
			}
		}
		t[0]=a;
		t[1]=b;
		return t;
	}


}