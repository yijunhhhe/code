import java.io.*;
import java.util.ArrayList;
public class SumOfTheDigits {

	public static void main(String arg[])throws Exception{

		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter the date(ddmmyy):");
		int number =Integer.parseInt(br.readLine());
		ArrayList<Integer> numberList = new ArrayList<Integer>();
		ArrayList<Integer> newSumList = new ArrayList<Integer>();
		int sum = 0;
		int i;
		do{
			numberList.add(number % 10);
			number = number / 10;
		} while(number > 0);
		
		for ( int integer: numberList )	{		
			sum = sum + integer;	}
		while (sum >= 10){
			newSumList.clear();
			do{
			
				newSumList.add(sum % 10);
				sum = sum / 10;
			
			}while(sum > 0);
			sum = 0;
			for ( int newInt: newSumList){					
				sum = sum + newInt;
			}		
		}
		System.out.println("Your lucky number is:"); 
		System.out.println(sum);
		
	}
			 
		
		
		   
		//main

}
