package Assignment1;

public class Country {
	
	private String name;
	private int population;
	private double area;
	private String continent;
	
	public Country(String name, int pop, double area, String con){
		this.name = name;
		this.population = pop;
		this.area = area;
		this.continent = con;
	}
	
	public String getName(){
		return this.name;
	}
	
	public int getPopulation(){
		return this.population;
	}
	
	public double getArea(){
		return this.area;
	}
	
	public String getContinent(){
		return this.continent;
	}

	public double getPopDensity(){
		return population/area;
	}
	
	public void setPopulation(int pop){
		this.population = pop;
	}
	
	public void writeToFile(ThingToWriteFile write){
		
		write.writeLine(String.format("%s, %s, %d, %f", name, continent, population, area));
		write.close();
				
	}
	
	public void printCountryDetails(){
		String detail;
		detail = String.format("%s is located in %s has "
				+ "a population of %d an area of %f and "
				+ "has a population density of %f", 
				name, continent, population, area, this.getPopDensity());
		System.out.println(detail);
	}
	
	public String toString(){
		return name + " in " + continent;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
