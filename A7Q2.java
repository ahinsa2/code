class A7Q2{
    public static void main (string[] args){
        //int[] ar=new int[10];
        int[] ar = {2, 5, 6, 5, 4, 3, 23, 43, 2, 0};
        int count=0;
        for (int i=0;i<=10-1;i++){
            count=0;
            for(int j=0;j<=10-1;j++){
               if(ar[i]==ar[j]){
                count+=1;}
                if(count>1){
                    System.out.println(ar[i]+" occurs "+count+" times.");           
                }
                else
                System.out.println(ar[i]+" occurs "+count+" time.");           
               
            }
        }
        
            

}}// 2 5 6 5 4 3 23 43 2 0