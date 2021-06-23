import java.util.*;
public class twodmerge{
	public static void main(String args[]){
		twodmerge obj=new twodmerge();
		Scanner sc=new Scanner(System.in);
		int m=sc.nextInt();
		int n=sc.nextInt();
		int ar[][]=new int[m][n];
		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++)
				ar[i][j]=sc.nextInt();
		}
		obj.sort(ar,0,m-1,0,n-1);
		for(int i=0;i<m;i++){
			for(int j=0;j<n;j++)
				System.out.print(ar[i][j]+" ");
		}
	}

	void sort(int ar[][],int ru,int rd,int cl,int cr){
		if(ru<rd && cl<cr){
			int t1=ru+ (rd-ru)/2;
			int t2=cl+ (cr-cl)/2;
			sort(ar,ru,t1,cl,t2);
			sort(ar,t1+1,rd,cl,t2);
			sort(ar,ru,t1,t2+1,cr);
			sort(ar,t1+1,rd,t2+1,cr);
			merge1(ar,ru,rd,cl,cr,t1,t2);
		}
		else if(ru<rd && cl>=cr){
			int t1=ru+ (rd-ru)/2;
			sort(ar,ru,t1,cl,cr);
			sort(ar,t1+1,rd,cl,cr);
			merge1(ar,ru,rd,cl,cr,t1,0);
		}
		else if(ru>=rd && cl<cr){
			int t2=cl+ (cr-cl)/2;
			sort(ar,ru,rd,cl,t2);
			sort(ar,ru,rd,t2+1,cr);
			merge1(ar,ru,rd,cl,cr,0,t2);
		}
	}

	void merge1(int ar[][],int ru,int rd,int cl,int cr,int t1,int t2){
		for(int i=ru;i<(rd+1);i++){
			int arr[]=new int[cr-cl+1];
			int k=0;
			for(int j=cl;j<cr+1;j++){
				arr[k]=ar[i][j];
				k++;
			}
			sort1(arr,0,k-1);
			int p=0;
			for(int j=cl;j<cr+1;j++){
				ar[i][j]=arr[p];
				p++;
			}
		}
		for(int i=cl;i<(cr+1);i++){
			int arr[]=new int[rd-ru+1];
			int k=0;
			for(int j=ru;j<rd+1;j++){
				arr[k]=ar[j][i];
				k++;
			}
			sort1(arr,0,k-1);
			int p=0;
			for(int j=ru;j<rd+1;j++){
				ar[j][i]=arr[p];
				p++;
			}
		}
	}

	void sort1(int arr[], int l, int r)
    {
        if (l < r) {
            int m =l+ (r-l)/2;
            sort1(arr, l, m);
            sort1(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }


	void merge(int arr[], int l, int m, int r){
        int n1 = m - l + 1;
        int n2 = r - m;
        int L[] = new int[n1];
        int R[] = new int[n2];
        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];
        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
}