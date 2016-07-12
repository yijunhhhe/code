import java.io.*;
import java.util.*;

public class NumberOccurrance2
{
	public static void main(String a[]) throws Exception
	{
         
          int[] arr = new int[8];
          int countOccurrence=0;
          Scanner scan=new Scanner(System.in);
          for(int i=0;i<8;i++)
          {
            System.out.println("Enter Number ["+i+"]:");
            arr[i]=scan.nextInt();   
          }
          System.out.println("Enter a number which exist in the array:");
          int number=scan.nextInt(); 
          for (int num : arr){
              if (num == number){
                  countOccurrence++;
              }
          }
          //write your logic here





           //end 
          System.out.println("Occurrence of "+number+" :");
          System.out.println(countOccurrence);

         
        }
} 
