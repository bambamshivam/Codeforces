import java.util.*;
public class hero{
	public static void main(String[] args) {
		hero obj=new hero();
		Scanner sc=new Scanner(System.in);
		long a=sc.nextLong();
		while(a-->0){
			long ha=sc.nextLong();
			long hh=sc.nextLong();
			int n=sc.nextInt();
			long ma[]=new long[n];
			long mh[]=new long[n];
			for(int i=0;i<n;i++)
				ma[i]=sc.nextLong();
			for(int i=0;i<n;i++)
				mh[i]=sc.nextLong();
			obj.sort(ma,mh,0,n-1);
			boolean flag=false;
			for(int i=0;i<n-1;i++){
				if(ma[i]>hh){
					flag=true;
					break;
				}
				else{
					long t=mh[i]/ha;
					if(t*ha<mh[i])
						t+=1;
					hh-=(ma[i]*t);
				}
			}
			if(flag==true)
				System.out.println("NO");
			else{
				long t=mh[n-1]/ha;
				if(t*ha<mh[n-1])
					t+=1;
				hh-=(ma[n-1]*(t-1));
				if(hh>0)
					System.out.println("YES");
				else
					System.out.println("NO");
			}
 
		}
	}
 
	static int partition(long arr[], long a[], int low, int high) 
    { 
        long pivot = arr[high];  
        int i = (low-1); 
        for (int j=low; j<high; j++) 
        { 
            if (arr[j] < pivot) 
            { 
                i++; 
                long temp = arr[i]; 
                arr[i] = arr[j]; 
                arr[j] = temp;
                long temp1=a[i];
                a[i]=a[j];
                a[j]=temp1; 
            } 
        } 
        long temp = arr[i+1]; 
        arr[i+1] = arr[high]; 
        arr[high] = temp; 
        long temp1=a[i+1];
        a[i+1]=a[high];
        a[high]=temp1;
  
        return i+1; 
    } 
  
    static void sort(long arr[], long a[],int low, int high) 
    { 
        if (low < high) 
        { 
            int pi = partition(arr, a, low, high); 
            sort(arr, a, low, pi-1); 
            sort(arr, a, pi+1, high); 
        } 
    } 	
}