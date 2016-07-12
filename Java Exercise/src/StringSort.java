import java.io.*;
import java.util.Arrays;
import java.util.*;
public class StringSort
{
	public static void main(String a[]) throws Exception
	{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	System.out.print("Enter a string:\n"); 	
	String str; 	 
	str=br.readLine();	
	
	//write your logic here 
	char[] charac = str.toCharArray();
	Arrays.sort(charac);
	str = "";
	for (char eachChar: charac){
		str = str + eachChar;
	}
	
	 

        
         
        //end 	
	
       System.out.println("Sorted string:\n"+ str);
        }
}
