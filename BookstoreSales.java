public class BookstoreSales {
    public static int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int baseSatisfied = 0;
        int extra = 0, windowSum = 0;

        for (int i = 0; i < customers.length; i++) {
            if (grumpy[i] == 0) baseSatisfied += customers[i];
        }

        for (int i = 0; i < customers.length; i++) {
            if (grumpy[i] == 1) windowSum += customers[i];
            if (i >= X && grumpy[i - X] == 1) windowSum -= customers[i - X];
            extra = Math.max(extra, windowSum);
        }
        return baseSatisfied + extra;
    }

    public static void main(String[] args) {
        int[] customers = {1,0,1,2,1,1,7,5};
        int[] grumpy = {0,1,0,1,0,1,0,1};
        System.out.println(maxSatisfied(customers, grumpy, 3)); // 16
    }
}
