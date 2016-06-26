package Assignment1;

public class Test {

	public static void main(String[] args) {
		/*// TODO Auto-generated method stub
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
		ThingToWriteFile write = new ThingToWriteFile("C:\\Users\\Ted\\Desktop\\code\\CS1027\\src\\Assignment1\\aaa.txt");
		canada.writeToFile(write);
		// test printCountryDetail method
		canada.printCountryDetails();*/
		
		
		CountryCatalogue catalogue = new CountryCatalogue("a","a");
		Country england = new Country("England", 43000000, 34658833, "North America");
		// test addCountry method
		catalogue.addCountry(england);
		// test removeCountry method
		catalogue.removeCountry("Japan");
		// test getCountry method
		Country country = catalogue.getCountry(2);
		System.out.println("The country we get is: " + country + "\n");
		// test fileterCountriesByContinent method
		catalogue.fileterCountriesByContinent("Asia");
		// test searchCatalogue/add&remove method
		int index = catalogue.searchCatalogue("England");
		System.out.println("The index is: " + index );
		index = catalogue.searchCatalogue("Japan");
		// test setPopulationOfACountry
		catalogue.setPopulationOfACountry("England", 123456789 );
		System.out.println("new population of England is: " + england.getPopulation());
		
		// test saveCountryCatalogue method
		catalogue.saveCountryCatalogue("C:\\Users\\Ted\\Desktop\\code\\CS1027\\src\\Assignment1\\output.txt");
		
		//System.out.println(country);
		//catalogue.fileterCountriesByContinent("Asia");
		//int index = catalogue.searchCatalogue("Japan");
		//System.out.println(index);
		//catalogue.removeCountry("Japan");
		
		
		//catalogue.printCountryCatalogue();
		//catalogue.printCountriesFileterDensity(30, 100);
		//catalogue.findMostPopulousContinent();
	}

}
