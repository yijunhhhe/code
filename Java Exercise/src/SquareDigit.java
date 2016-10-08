/*Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
*/


public class SquareDigit {
	public static int squareDigits(int n) {
		String number = Integer.toString(n);
		String newNum = "";
		
		for (int i = 0; i < number.length(); i++){
			int digit = Character.getNumericValue(number.charAt(i));
			newNum = newNum + "" + digit * digit;
		}
		
		
		return Integer.parseInt(newNum);
		
	}
	
	public static void main(String[] args){
		System.out.println(squareDigits(9119));
	}
	
}
/*
 * Alternative solution
public class SquareDigit {

	  public int squareDigits(int n) {
	    String result = ""; 
	    
	    while (n != 0) {
	      int digit = n % 10 ;
	      result = digit*digit + result ;
	      n /= 10 ;
	    }
	    
	    return Integer.parseInt(result) ;
	  }

	}
	*/
