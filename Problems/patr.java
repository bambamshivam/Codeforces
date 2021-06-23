/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class patr
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
		    int n=sc.nextInt();
		    for(int i=0;i<n;i++){
		        for(int j=0;j<=i;j++){
		            System.out.print(j+1);
		            if(j+1<=i){
		                for(int k=0;k<=j;k++)
		                System.out.print("*");
		            }
		        }
		        System.out.println();
		    }
		}
	}
}
