package Assignment1;

/**
 * 
 * class represents a country with different elements
 * including name, population, area, continent, population density
 * @author Yijun He
 * 
 **/
public class Country {
	
	/*
	 * name of the country
	 */
	private String name;
	
	/*
	 * population of the country
	 */
	private int population;
	
	/*
	 * area of the country
	 */
	private double area;
	
	/*
	 * continent of the country
	 */
	private String continent;
	
	/*
	 * Constructor read name, population, area, and continent 
	 * then store them in the corresponding instance variable
	 * @param name name of the country
	 * @param pop population of the country
	 * @param area area of the country
	 * @param con continent of the country
	 */
	public Country(String name, int pop, double area, String con){
		this.name = name;
		this.population = pop;
		this.area = area;
		this.continent = con;
	}
	
	/*
	 * get the name of the country
	 * @return name of the country
	 */
	public String getName(){
		return this.name;
	}
	
	/*
	 * get the population of the country
	 * @return population of the country
	 */
	public int getPopulation(){
		return this.population;
	}
	
	/*
	 * get the area of the country
	 * @return area of the country
	 */
	public double getArea(){
		return this.area;
	}
	
	/*
	 * get the continent of the country
	 * @return continent of the country
	 */
	public String getContinent(){
		return this.continent;
	}

	/*
	 * get the population density of the country
	 * @return population divided by area
	 */
	public double getPopDensity(){
		return population/area;
	}
	
	/*
	 * set a new population to the country
	 * @param pop new population
	 */
	public void setPopulation(int pop){
		this.population = pop;
	}
	
	/*
	 * write line to a file
	 * @param write a variable of ThingToWriteFile
	 */
	public void writeToFile(ThingToWriteFile write){		
		write.writeLine(String.format("%s, %s, %d, %f\n", name, continent, population, area));					
	}
	
	/*
	 * print the detail of a country
	 * including name, continent, population, area, and population density
	 */
	public void printCountryDetails(){
		String detail;
		detail = String.format("%s is located in %s has "
				+ "a population of %d an area of %f and "
				+ "has a population density of %f", 
				name, continent, population, area, this.getPopDensity());
		System.out.println(detail);
	}
	
	/*
	 * the output of a country object
	 * @return country name + "in" + country continent
	 */
	public String toString(){
		return name + " in " + continent;
	}

}
