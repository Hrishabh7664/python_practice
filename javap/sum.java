
import java.util.*;

public class sum {
    public static void main(String[] args){
        System.out.print("enter first number:");
        Scanner sc =new Scanner(System.in);
        int a = sc.nextInt();
        
        System.out.println("enter second number:");

        int b = sc.nextInt();
        int sum = a+b;

        System.out.println("sum of two numbers is:"+sum);  
    }
}