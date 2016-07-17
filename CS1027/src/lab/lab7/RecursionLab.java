import java.io.*;

public class RecursionLab{
    
    public static void reversePrint (String inString){
       
		if (inString.length() > 0)		// if string is not empty
		{
			System.out.print(inString.substring(inString.length()-1));
			inString = inString.substring(0, inString.length()-1);
			reversePrint(inString);	
		} else {
			return;
		}
    }
    
    public static String reverseString(String inString){
    	String result;
    	if (inString.isEmpty()){
    		return "";
    	} else {
    		result = inString.substring(inString.length()-1);
    	    inString = inString.substring(0, inString.length()-1);
    		result = result + reverseString(inString);
    		return result;
    	}
    	
    	
    }
	    
    public static void main(String[] args){
        String inString = "abcde";

		// test reversePrint
		reversePrint(inString);	
		System.out.println();		
		System.out.println(reverseString(inString));
    }
}
