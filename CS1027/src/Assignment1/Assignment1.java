
public class Assignment1 {

	public static void main(String[] args) {
		
		CountryCatalogue cc = new CountryCatalogue("data.txt", "continent.txt");
		Country cntry;
		
		cntry = cc.getCountry(cc.searchCatalogue("Canada"));
		if(cntry != null){
			cntry.printCountryDetails();
		}
		
		cntry = cc.getCountry(cc.searchCatalogue("USA"));
		if(cntry != null){
			cntry.printCountryDetails();
		}
		
		cntry = new Country("England", 54316600, 130279, "Europe");
		cc.addCountry(cntry);
		
		cntry = cc.getCountry(cc.searchCatalogue("England"));
		if(cntry != null){
			cntry.printCountryDetails();
		}
		
		cc.removeCountry("England");
		cntry = cc.getCountry(cc.searchCatalogue("England"));
		if(cntry != null){
			cntry.printCountryDetails();
		}
		
		cc.printCountryCatalogue();
		System.out.print("Country with the largest population: ");
		cc.getCountry(cc.findCountryWithLargestPop()).printCountryDetails();
		System.out.print("Country with the smallest area: ");
		cc.getCountry(cc.findCountryWithSmallestArea()).printCountryDetails();
		cc.filterCountriesByContinent("North America");
		System.out.println();
		cc.printCountriesFilterDensity(0, 25);
		cc.findMostPopulousContinent();
		cc.saveCountryCatalogue("outDetails.txt");
	}
}
