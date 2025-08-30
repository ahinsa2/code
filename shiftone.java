class Shiftone{
    public static void main (String[] args){
        int[] ar={1,3,4,6};
        int temp=0;
        temp=ar[0];
        for (int i=0;i<ar.length-1;i++){
            ar[i]=ar[i+1];
        }
        ar[ar.length-1]=temp;
        for(int i=0;i<ar.length;i++){
           System.out.print(ar[i]+" ");
        }
        
    
        
    }
}
