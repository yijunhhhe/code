import java.io.*;
import java.util.Iterator;
/**
 * PhoneTest.java:
 * This class creates an Ordered List of Phone objects.
 * @author CS1027 for Lab
 */

public class PhoneTest {

   public static void main(String[] args) throws Exception {

   // get the filename from the user
     
      BufferedReader keyboard = new BufferedReader
                                 (new InputStreamReader(System.in),1);       
      System.out.println("Enter name of the input file: ");
      String filename= keyboard.readLine();
    
   // create object that controls file reading and opens the file
         
      InStringFile reader = new InStringFile(filename);
      System.out.println("\nReading from file " + filename + "\n");

    // your code to create (empty) ordered list here
      ArrayOrderedList<Phone> orderedList = new ArrayOrderedList<Phone>();
      
   // read data from file two lines at a time (name and phone number)
     
      String name, phone;
      do {
        name = (reader.read());
        phone = (reader.read());

        // your code to add the entry to your ordered list here
        Phone newPhone = new Phone(name,phone);
        orderedList.add(newPhone);
        


              
      } while (!reader.endOfFile()); 
   
      System.out.println("Here is my phone book:");

      // your code to print the ordered list here
      System.out.println("Exercise 1:");
      Iterator<Phone> itr = orderedList.iterator();
      while(itr.hasNext()){      
    	  System.out.println(itr.next().getName()); 
    	  
      }
      
      itr = orderedList.iterator();
      while(itr.hasNext()){      
    	  System.out.println(itr.next().getPhone());    	  
      }
      
      System.out.println("\nExercise 2:");
      System.out.println(orderedList.toString2());
      
   // close file
      
      reader.close();
      System.out.println("\nFile " + filename + " is closed.");      
     
   }
   // question
   // you need a LinkedIterator file, listADT file,  LinkedList file, LinkedOrderedList file
   // nothing
   // Yes
}
