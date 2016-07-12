import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Scanner;
public class CountOne
{
public static void main(String[] args)
{
 
	  System.out.println("Enter the Maximum value:");
	  Scanner sc1 = new Scanner(System.in);
	  long min = sc1.nextLong();
	  long max = sc1.nextLong();
	
	  int count=0;
	  char[] number;
	
	  for(int i=(int)min ; i<=(int)max;i++){
		  number = new char[Integer.toString(i).length()];
		  number = Integer.toString(i).toCharArray();
		  for(int j = 0; j<Integer.toString(i).length(); j++){
			  if (Character.getNumericValue(number[j]) == 1){
				  count++;
			  }
		  }
	  }
	  System.out.println("Total sum of count of 1s: " + count); 

}
}










