class Test{
    public static void main(String[] args){
        int[] ar={1,3,3,5,7,9,3,9,0,5};
        int num=9;
        int count=0;
        for (int i=0;i<=10-1;i++){
           if(ar[i]==num){
            count++;
           }
        }
        System.out.println(num+" is repeated "+count+" times.");
    }
}/*Input 10 integers from the keyboard into an array. The number to be searched is entered through 
the keyboard by the user. Write a java program to find if the number to be searched is present in 
the array and if it is present, display the number of times it appears in the array. */
