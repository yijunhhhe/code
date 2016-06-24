

public class StringMethod {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String greeting = "Hello World";
		
		// length
		int length = greeting.length(); 
		System.out.println( "String Length is : " + length );
		
		// concatenating strings
		String newStr = greeting.concat("wth");
		newStr = newStr + "Yes";
		System.out.println("Concatenation" + newStr);
		
		// format String
		String fs;
		fs = String.format("The value of the float variable is " +
                ", while the value of the integer " +
                "variable is %d, and the string " +
                "is %s", length, newStr);
		
		// Method
		String s = "Strings are immutable";
	    char result = s.charAt(8); // character at the specified index
	    
	    String Str = new String("This is really not immutable!!");
	    boolean retVal;
	    retVal = Str.endsWith( "immutable!!" );  //endswith

	    String Str1 = new String("This is really not immutable!!");
	    String Str3 = new String("This is really not immutable!!");
	    retVal = Str1.equals( Str3 );  //equal
	    
	    String Str = new String("Welcome to Tutorialspoint.com");
	    System.out.println(Str.indexOf( 'o' ));  // index of char
	    System.out.println(Str.indexOf( 'o', 5 ));
	    
	    System.out.println(Str.substring(10) );  // return a substring
	    
	    System.out.println(Str.toLowerCase());  // return lower case
	    
	    System.out.println(Str.toCharArray() );  // return an array of char
	    
	    System.out.println(Str.toUpperCase() );  // return upper case

	    System.out.println(Str.trim() );  // strip the leading and trailing white space in python 
	
	    System.out.println("Return Value :" );
	      for (String retval: Str.split("-", 2)){  // split
	         System.out.println(retval);}
	      
	    System.out.println(Str.replaceFirst("Tutorials", "AMROOD" )); // replace 
	    System.out.println(Str.replace('o', 'T'));
	}

}
