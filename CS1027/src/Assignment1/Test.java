package Assignment1;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Country canada = new Country("canada", 43000000, 34658833, "North America");
		String name = canada.getName();
		double area = canada.getArea();
		int pop = canada.getPopulation();
		String continent = canada.getContinent();
		double popDensity = canada.getPopDensity();
		System.out.println(String.format("%s, %f, %d, %s", name, area, pop, continent));
		// test set method
		canada.setPopulation(34000000);
		pop = canada.getPopulation();
		System.out.println(pop);
		//test toString method
		System.out.println(canada);
		//test writeToFile method
		ThingToWriteFile write = new ThingToWriteFile("C:\\Users\\tambe\\Desktop\\code\\CS1027\\src\\Assignment1\\aaa.txt");
		canada.writeToFile(write);
		// test printCountryDetail method
		canada.printCountryDetails();
		
		
		
	}

}
