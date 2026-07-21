import java.util.*;


public class ITJ5 {
    public static void main(String[] args){
        System.out.print("enter height of rectangle:");
        Scanner sc = new Scanner(System.in);
        float height = sc.nextFloat();
        System.out.print("enter width of rectangle:");
        float width = sc.nextFloat();

        float area = height * width;
        float perimeter = 2 * (height + width);

        System.out.println("Area of the rectangle is: " + area);
        System.out.println("Perimeter of the rectangle is: " + perimeter);

    }
}