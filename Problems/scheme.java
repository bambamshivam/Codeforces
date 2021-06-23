import java.util.*;
public class scheme{
	public static void main(String args[]){
		scheme obj=new scheme();
		Scanner sc=new Scanner(System.in);
		int minmarks=sc.nextInt();
		int s=sc.nextInt();
		int n=sc.nextInt();
		Ques[] ar=new Ques[n];
		int sess[]=new int[s];
		for(int i=0;i<s;i++)
			sess[i]=sc.nextInt();
		for(int i=0;i<n;i++){
			int m=sc.nextInt();
			int p=sc.nextInt();
			ar[i]=new Ques(m,p,i);
		}
		obj.sort(ar,0,n-1);
		ArrayList<Integer>[] choice=new ArrayList[s];
		for(int i=0;i<s;i++){
			choice[i]=new ArrayList<Integer>();
			int t=minmarks-sess[i];
			int c=0;
			int sum=0;
			while(sum<t && c<ar.length){
				sum=sum+ar[c].max;
				choice[i].add(ar[c].order);
				c++;
			}
		}
		for(int i=0;i<s;i++)
			Collections.sort(choice[i]);
		for(int i=0;i<s;i++){
			System.out.print(choice[i].size()+" ");
			for(int j=0;j<choice[i].size();j++)
				System.out.print(choice[i].get(j)+1+" ");
			System.out.println();
		}
	}

    void merge(Ques arr[], int l, int m, int r){
        int n1 = m - l + 1;
        int n2 = r - m;
        Ques L[] = new Ques[n1];
        Ques R[] = new Ques[n2];
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];
        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i].sub > R[j].sub) {
                arr[k] = L[i];
                i++;
            }
            else if(L[i].sub==R[j].sub){
            	double d1=(double)(L[i].max)/L[i].sub;
            	double d2=(double)(R[j].max)/R[j].sub;
            	if(d1<=d2){
	                arr[k] = L[i];
	                i++;
	            }
	            else{
	            	arr[k]=R[j];
	            	j++;
	            }
            }
            else{
            	arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1){
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2){
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    void sort(Ques arr[], int l, int r){
        if (l < r) {
            int m =l+ (r-l)/2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

	static class Ques{
		int max;
		int sub;
		int order;
		Ques(int max,int sub,int order){
			this.max=max;
			this.sub=sub;
			this.order=order;
		}
	}
}