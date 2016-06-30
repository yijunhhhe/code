import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
public class StamentReverse
{
	public static void main(String a[]) throws Exception
	{
		String strarr[];    //array which will hold splitted strings of the statement
        String st;      //contains user input statement 
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the Statement:"); 
        st=br.readLine();
        strarr = st.split(" ");
        
        ArrayList<String> newStr = new ArrayList<String>();
        for (int i = strarr.length - 1; i >= 0 ; i--){
        	newStr.add(strarr[i]);
        }
        st = "";
        for (String s: newStr){
        	st = st + s + " ";
        }
        System.out.println("The reverse is:" + st);
        

      
   /*write down your logic here*/ 
        System.out.println(st);
 	 
        } 
	 
}  
   
 




