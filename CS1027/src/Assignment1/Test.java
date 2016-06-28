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
		Country england = new Country("England", 43000000, 34658833, "Europe");
		
		// test addCountry method
		catalogue.addCountry(england);
		
		// test removeCountry method
		catalogue.removeCountry("Japan");
		catalogue.removeCountry("New Zealand");
		
		// test getCountry method
		Country country = catalogue.getCountry(2);
		System.out.println("The country we get is: " + country);
		country = catalogue.getCountry(17);
		System.out.println("The country we get is: " + country + "\n");
			
		// test fileterCountriesByContinent method
		catalogue.fileterCountriesByContinent("Asia");
		
		// test searchCatalogue/add&remove method
		int index = catalogue.searchCatalogue("England");
		System.out.println(catalogue.getCatalogue()[index].getName() + " index is: " +  index );
		index = catalogue.searchCatalogue("Japan");
		
		
		// test printCountryCatalogue method
		catalogue.printCountryCatalogue();
		
		// test setPopulationOfACountry
		catalogue.setPopulationOfACountry("England", 123456789 );
		catalogue.setPopulationOfACountry("Germany", 123456789 );
		
		// test saveCountryCatalogue method
		catalogue.saveCountryCatalogue("C:\\Users\\Ted\\Desktop\\code\\CS1027\\src\\Assignment1\\output.txt");
		
		// test findCountryWithLargestPop method
		int larPop = catalogue.findCountryWithLargestPop();
		int pop = catalogue.getCatalogue()[larPop].getPopulation();
		String name = catalogue.getCatalogue()[larPop].getName();
		System.out.println("Country with the largest population: " + name + " has a population of " + pop + "\n");
		
		// test findCountryWithSmallestPop method
		int smallArea = catalogue.findCountryWithSmallestArea();
		double area = catalogue.getCatalogue()[smallArea].getArea();
		name = catalogue.getCatalogue()[smallArea].getName();
		System.out.println("Country with the smallest Area: " + name + " has an area of " + area + "\n");
		
		// test printCountriesFilterDensity method
		catalogue.printCountriesFilterDensity(0, 25);
		
		// test findMostPopulousContinent method
		catalogue.findMostPopulousContinent();
		
		
		
		
	}

}
