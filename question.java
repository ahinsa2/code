class A7Q4{
    public static void main(String[] args){
        double[] array={1.0,3.0,3.0,5.0,7.0,9.0,3.0,9.0,0.0,5.0};
        System.out.println(min(array));
    }
    public static double min(double[] ar){
        int min=ar[0];
        for (int i=0;i<=ar.length-1;i++){
            if(ar[i]<min){
                min=ar[i];
            }
        }
        return min;

    }
}
