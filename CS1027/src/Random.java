import java.io.*;

public class Random {
	
	
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String fileName = "C:/Users/tambe/Desktop/code/CS1027/src/aa.txt";
		FileReader fileReader = new FileReader(fileName);
		BufferedReader textReader = new BufferedReader(new FileReader(fileName));
		BufferedWriter textWriter = new BufferedWriter(new FileWriter(fileName));
		// Write 
		textWriter.write("what the fuck\n");
		textWriter.write("woooo");
		textWriter.close();
		// Read
		String[] arrays = new String[4];
		for( int i = 0; i < 4; i++){
			arrays[i] = textReader.readLine();
			System.out.println(arrays[i]);
		}
		
		
		
		
		
		
		
	}

}
