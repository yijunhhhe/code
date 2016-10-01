import java.util.Scanner;

public class practice{
	public static void main(String[] args){	
	String s = "adsfasdf";
	boolean found = false;
	int position = 0;
	while (!found && position < s.length()){
		if (Character.isDigit(s.charAt(position)) == true){
			found = true;			
		}else {
			position = position + 1;
		}
	}
	if (found == true){
		System.out.println(position);
	}else {
		System.out.println("not found");
	}
	
	}
}