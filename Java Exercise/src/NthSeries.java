import java.text.DecimalFormat;
import java.util.Scanner;

public class NthSeries {

	public static String seriesSum(int n) {
		
		if(n == 1){ 
			return "1";}
		
		double total = 0.00;
		int b = 1;
		double divide;
		for (int i = 1; i <= n; i++ ){
			divide = 1.00 / b;
			total = total + divide;
			b = b + 3;
		}
		double totalOff = Math.round(total * 100.00) / 100.00;
		String off = String.format("%.2f", total);
		return off;
		
	}
	public static void main(String[] args) {
		System.out.format( seriesSum(80));

	}

}
