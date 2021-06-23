import java.util.*;
class alcm{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		alcm obj=new alcm();
		int t=sc.nextInt();
		while(t-->0){
			int n=sc.nextInt();
			int k=sc.nextInt();
			int ar[]=new int[n];
			int lcm=1;
			for(int i=0;i<n;i++){
				ar[i]=sc.nextInt();
				lcm=obj.lc(lcm,ar[i]);
				if(lcm>k)
					break;
			}
			System.out.println(k/lcm);
		}
	}

	int gcd(int a, int b)
    {
        if (a == 0)
            return b;
        return gcd(b % a, a);
    }

    int lc(int a, int b)
    {
        return (a / gcd(a, b)) * b;
    }
}