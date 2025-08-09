class A7Q5{
    public static void main(String[] args){
        int[] ar={1,2,5,7,3,6,3,6,68};
        int largest=ar[0];
        for(int i=0;i<=ar.length-1;i++){
            if(ar[i]>largest){
                largest=ar[i];
            }            
        }
        int largest2=ar[0];
        for(int i=0;i<=ar.length-1;i++){
            if(ar[i]>largest2 && ar[i]!=largest){
                largest2=ar[i];
            } 
        }
        System.out.println(largest2);
    }
}
