import java.util.*;
public class game{
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		while(a-->0){
			String s=sc.next();
			String str="";
			for(int i=0;i<s.length();i++){
				if(i%2==0){
					if(s.charAt(i)!='a')
						str+='a';
					else
						str+='b';
				}
				else{
					if(s.charAt(i)!='z')
						str+='z';
					else
						str+='y';
				}
			}
			System.out.println(str);
		}
	}
}