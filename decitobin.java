public class DecimalToBinary {
    public static void main(String[] args) {
        int decimal = 25; // You can change this number to test different values
        String binary = "";

        if (decimal == 0) {
            binary = "0";
        } else {
            int num = decimal;
            while (num > 0) {
                binary = (num % 2) + binary;
                num = num / 2;
            }
        }

        System.out.println("Decimal: " + decimal);
        System.out.println("Binary: " + binary);
    }
}
