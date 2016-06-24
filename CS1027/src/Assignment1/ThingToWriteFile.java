package Assignment1;

import java.io.*;
/**
 * ThingToWriteFile makes file writing simpler. It allows
 * information to be written one line at a time to a
 * data file
 * @author CS1027
 */
public class ThingToWriteFile {
	
	private BufferedWriter out;
	
	/**
	* Constructs the object that controls file writing
	* Exits gracefully if file not found or file cannot be read
	* @param filename the name of the file to be read
	*/
	public ThingToWriteFile(String filename) {   
		try {   	
			out = new BufferedWriter(new FileWriter(filename));
		}
		catch (FileNotFoundException ee){
			System.out.println("File " + filename + " not found.");
			System.exit(0);
		}
		catch (IOException e){
			System.out.println("File " + filename + " cannot be read.");
			System.exit(0);
		}
	}
	
	/**
	* Writes a line to the file
	* Exits gracefully if an error occurs while reading the file
	* @param line the line to be written to the file.
	*/ 
	public void writeLine(String line){
		try{
			out.write(line);
		}
		catch (IOException e){
			System.out.println("File cannot be written too.");
			System.exit(0);
		}
	}
	
	/**
	* Closes the file (making it inaccessible though this ThingToWriteFile)
	*/
	public void close(){
		try {
			out.close();
			out = null;
		}
		catch (IOException e){
			System.out.println("Problem closing file.");
			System.exit(0);
		}
	}
}
