
public class Random {
	
	public static final class City{
		String name;
		String cityType;
		double population;
		double area;
		String province;
		public City(String name, String cT, double pop, double area, String pro){
			this.name = name;
			this.cityType = cT;
			this.population = pop;
			this.area = area;
			this.province = pro;
		}
		
		public double getPopulation(){
			return population;
		}
		public String getName(){
			return name;
		}
		public double getArea(){
			return area;
		}
		
		
		
	}
	
	public static void dd(){
		System.out.println("Hey");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		City city ;
		city = new City( "London", "City", 450.0, 460.0, "Ontario");
		System.out.println(city);
		System.out.println(city.getPopulation());
		
		dd();
	}

}
