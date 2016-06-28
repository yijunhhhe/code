import java.util.Scanner;

public class IsBinaryOrNot {
	public static void main(String a[]) throws Exception  
	{  
		int num;
        System.out.println("Enter a number:");
	Scanner sc = new Scanner(System.in);
	num = sc.nextInt();
	    char[] newChar = Integer.toString(num).toCharArray();
	    int number = 0;
	    
	    for (char char1: newChar){
	        if (Character.getNumericValue(char1) > 1 || Character.getNumericValue(char1) < 0 ){
	            number = number + 1;
	        } else  number = number + 0;
	    }
	    
        if (number >= 1 ){
        	System.out.println("Not Binary");
        } else System.out.println("Binary");

	System.out.println("The number is:" + num + "");
  
  
  
  
    
  
        } 
}
