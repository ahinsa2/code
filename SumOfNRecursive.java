import java.util.Scanner;

public class SumOfNRecursive {
    public static int sumOfN(int n) {
        if (n == 0)
            return 0;
        return n + sumOfN(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = sc.nextInt();
        System.out.println("Sum of first " + n + " numbers: " + sumOfN(n));
        sc.close();
    }
}
