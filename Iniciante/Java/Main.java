package Java;

import java.util.Scanner;
import java.text.DecimalFormat;
public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        double n1 = scan.nextFloat();
        double n2 = scan.nextFloat();
        double media = ((n1 * 3.5) + (n2 * 7.5))/11;
        DecimalFormat df1005 = new DecimalFormat("#.00000");
        System.out.println("MEDIA = " + df1005.format(media));
    }
}