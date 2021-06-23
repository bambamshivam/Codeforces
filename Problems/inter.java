import java.util.*;
class inter{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			String str=sc.next();
			int b=0;
			if(str.contains("e") && str.contains("E"))
				b=1;
			if(str.charAt(0)=='e' || str.charAt(0)=='E')
				str=str.substring(1,str.length());
			if(str.charAt(str.length()-1)=='e' || str.charAt(str.length()-1)=='E')
				str=str.substring(0,str.length()-1);
			if(b==1 && str.contains("C") && str.contains("o") && str.contains("D") && str.contains("e"))
				System.out.println("SELECTED");
			else 
				System.out.println("REJECTED");
		}
	}
}