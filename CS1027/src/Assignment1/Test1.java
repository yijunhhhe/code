package Assignment1;

public class Test1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CountryCatalogue catalogue = new CountryCatalogue("a","a");
		Country england = new Country("England", 43000000, 34658833, "North America");
		catalogue.removeCountry("Japan");
		int index = catalogue.searchCatalogue("Japan");
	}

}
