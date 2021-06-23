import java.util.Scanner;

public class teams{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int a=sc.nextInt();
        int b=a;
        int p=0;
        while(a-- > 0){
            int a1=sc.nextInt();
            int a2=sc.nextInt();
            int a3=sc.nextInt();
            if(a1*a2==0 && a3==0 || (a1*a3==0 && a2==0) || (a2*a3==0 && a1==0))
            p++;
        }
        System.out.println(b-p);
    }
}