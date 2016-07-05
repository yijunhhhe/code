import java.io.*;
import java.util.Scanner;
import java.util.Arrays;
public class NameSearch {
	public static String names[]={"harry","michael","will","tom","jackie"};    
    public static String surnames[]={"potter","jackson","smith","cruise","chan"};    
    public static void main(String a[]) throws Exception
    {
    	Scanner sc=new Scanner(System.in);
    	String name;   
    	int index = 0;
  
    	System.out.println("Enter the name:");
    	name=sc.next();
    	for(int i = 0; i < 5; i++){
    		if (names[i].equals(name)){
    			index = Arrays.asList(names).indexOf(name);
    			name = name + " " + surnames[index];
    			break;
    		}
    	}
    	
      
    	System.out.println("Full name of the celebraty is: ");
    	/*write down your logic*/
    	System.out.println(name);
    	
    	
    	
    	
    }//main 





}
