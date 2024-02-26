package Java;
import java.util.Scanner;
import java.lang.Math;
import java.text.DecimalFormat;

public class Iniciante{
    public static void main(String[] args){

        // 1000 - Hello World!
        // System.out.println("Hello World!");

        // // 1001 - Extremamente Básico
        // Scanner J1001 = new Scanner(System.in);
        // int a = J1001.nextInt();
        // int b = J1001.nextInt();
        // J1001.close();
        // System.out.println("X = " + (a+b));

        // // 1002 - Área do Círculo
        // Scanner J1002 = new Scanner(System.in);
        // double raio = J1002.nextDouble();
        // J1002.close();
        // double area = 3.14159 * (Math.pow(raio, 2));
        // DecimalFormat df = new DecimalFormat("#.0000");
        // System.out.println("A=" + df.format(area));

        // // 1003 - Soma Simples
        // Scanner J1003 = new Scanner(System.in);
        // int a = J1003.nextInt();
        // int b = J1003.nextInt();
        // J1003.close();
        // System.out.println("SOMA = " + (a+b));

        // 1004 - Produto simples
        Scanner J1004 = new Scanner(System.in);
        int a = J1004.nextInt();
        int b = J1004.nextInt();
        J1004.close();
        System.out.println("PROD = " + (a*b));
    }
}

