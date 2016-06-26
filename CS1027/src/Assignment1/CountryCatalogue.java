package Assignment1;
import java.util.*;

public class CountryCatalogue {
	private final int DEFAULT_SIZE = 5;
	private final int NOT_FOUND = -1;
	private Country[] catalogue = new Country[DEFAULT_SIZE];
	private int numberOfCountries = 0;
	Set<String> continent = new HashSet<String>();
	Map<String,String> cDic = new HashMap<String,String>();
	
	public Country[] getCatalogue(){
		return catalogue;
	}
	
	public CountryCatalogue(String dFileN, String cFileN){
		String dataFileName = dFileN;
		String continentFileName = cFileN;
		String line;
		String firstLine;
		String[] lineInfo = new String[3];
		ThingToReadFile readCountry = new ThingToReadFile("C:\\Users\\Ted\\Desktop\\code\\CS1027\\src\\Assignment1\\data.txt");
		ThingToReadFile readContinent = new ThingToReadFile("C:\\Users\\Ted\\Desktop\\code\\CS1027\\src\\Assignment1\\continent.txt");
		
		firstLine = readContinent.readLine();
		while((line = readContinent.readLine()) != null){
			lineInfo = line.split(",");
			cDic.put(lineInfo[0], lineInfo[1]);
			if (!continent.contains(lineInfo[1])){
				continent.add(lineInfo[1]);
			}
		}	
		
		firstLine = readCountry.readLine();
		while ((line = readCountry.readLine()) != null){			
			lineInfo = line.split(",");			
			Country country = new Country(lineInfo[0], Integer.parseInt(lineInfo[1]), Double.parseDouble(lineInfo[2]), cDic.get(lineInfo[0]) );
			addCatalogue(country);
		}
		readCountry.close();
		readContinent.close();
		
	}
	
	public void addCatalogue(Country country){
		catalogue[numberOfCountries] = country;
		numberOfCountries++;
		if (numberOfCountries >= catalogue.length){
			expandCapacity(catalogue);			
		}
	}
	
	public void expandCapacity(Country[] catalogue){
		Country[] newCatalogue = new Country[catalogue.length*2];
		for(int i = 0; i < catalogue.length ; i++){
			newCatalogue[i] = catalogue[i];
		}
		this.catalogue = newCatalogue;		
	}
	
	public void addCountry(Country country){
		addCatalogue(country);
		if (Arrays.asList(catalogue).contains(country)){
			System.out.println(String.format("The country I add: %s is located in "
				+ "%s has a population of %d,\n an area of %f, "
				+ "and has a population density of %f", 
				country.getName(), country.getContinent(), country.getPopulation(), country.getArea(), country.getPopDensity()));
		System.out.println("");
		} else {
			System.out.println(country.getName() + "is not added successfully.");
		}
		if (!continent.contains(country.getContinent())){
			continent.add(country.getContinent());
		}
		cDic.put(country.getName(), country.getContinent());
	}
	
	public Country getCountry(int index){		
		return catalogue[index];
	}
	
	public void printCountryCatalogue(){
		System.out.println("Country Catalogue:");
		for (int i = 0; i < numberOfCountries; i++){
			System.out.println(catalogue[i]);
		}
		System.out.println("");
	}
	
	public void fileterCountriesByContinent(String continent){
		System.out.println("Countries in " + continent);
		for (int i = 0; i < numberOfCountries; i++){
			if (catalogue[i].getContinent().equals(continent) ){
				System.out.println(catalogue[i] );				
			}
		}
		System.out.println("");
	}
	
	public int searchCatalogue(String countryName){
		boolean found = false;
		for (int i = 0; i < numberOfCountries; i++){
			if (catalogue[i].getName().equals(countryName)){
				return i;
			} 			
		}	
		System.out.println(countryName + " was not found.");
		System.out.println("");			
		return NOT_FOUND;
	}
	
	public void removeCountry(String countryName){
		int found = searchCatalogue(countryName);
		if (found != -1){
			//Country newCountry = 
			catalogue[found] = catalogue[numberOfCountries-1];
			catalogue[numberOfCountries] = null;
			numberOfCountries--;
			System.out.println(countryName + " has been successfully removed.");
			System.out.println("");
		}
	}
	
	public void setPopulationOfACountry(String countryName, int newPop){
		int found = searchCatalogue(countryName);
		if (found != -1){
			catalogue[found].setPopulation(newPop);	
			System.out.println("the country has been successfully altered");
			System.out.println("new population of " + countryName + "is: " + catalogue[found].getPopulation());
			System.out.println("");
		} 
	}
	
	public void saveCountryCatalogue(String fileName){
		ThingToWriteFile write = new ThingToWriteFile(fileName);
		
		for (int i = 0; i < numberOfCountries; i++){
			catalogue[i].writeToFile(write);
		}
		write.close();
	}
	
	public int findCountryWithLargestPop(){
		int largest = 0;
		int index = 0;
		for (int i = 0; i < numberOfCountries; i++){
			if (catalogue[i].getPopulation() > largest ){
				largest = catalogue[i].getPopulation();
				index = i;
			}
		}
		return index;
	}
	
	public int findCountryWithSmallestArea(){
		double smallest = 1999999999;
		int index = 0;
		for (int i = 0; i < numberOfCountries; i++){
			if (catalogue[i].getArea() < smallest) {
				smallest = catalogue[i].getArea();
				index = i;
			}			
		}
		return index;
	}
	
	public void printCountriesFilterDensity(int low, int high){
		System.out.println("Countries with a population density between " + low + " and " + high);
		for (int i = 0; i < numberOfCountries; i++){
			if (catalogue[i].getPopDensity()> low && catalogue[i].getPopDensity() < high){
				System.out.println("          " + catalogue[i]);
				System.out.println("          has a population density of " + catalogue[i].getPopDensity());
				System.out.println("");
			}
		}
	}
	
	public void findMostPopulousContinent(){
		Set<String> continentSet = new HashSet<String>();	
		Map<String, ArrayList<Integer>> continentMap = new HashMap<String, ArrayList<Integer>>();
		Map<String, Integer> popMap = new HashMap<String, Integer>();
		int max = 0;
		String name = "";
		for (int i = 0; i < numberOfCountries; i++){
			continentSet.add(catalogue[i].getContinent());
		}
		for (String continent: continentSet){
			continentMap.put(continent, new ArrayList<Integer>() );
		}
		for (String continent: continentSet){
			for (int i = 0; i < numberOfCountries; i++){
				if (catalogue[i].getContinent().equals(continent)){
					continentMap.get(continent).add(catalogue[i].getPopulation());
				}
			}
		}	
		for (String continent: continentSet){
			popMap.put(continent, sum(continentMap.get(continent)));
		}		
		for (String continent: popMap.keySet()){
			if (popMap.get(continent) > max){
				max = popMap.get(continent);
				name = continent;
			}		
		}
		System.out.println("The most populous continent in our catalogue is " + name + " with " + popMap.get(name) + " people");
	}
	
	private Integer sum(ArrayList<Integer> arrayList) {
		int sum = 0;
		for(int d : arrayList)
		    sum += d;
		return sum;		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}

}
