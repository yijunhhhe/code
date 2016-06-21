
public class Random {
	
	public static void get(){
		Random random = new Random();
		City city = random.new City("London", "City", 500, 460.0, "Ontario");
		System.out.println(city.getArea());
	}	

	public class City{
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
		Random random = new Random();
		City city ;
		city = random.new City( "London", "City", 450.0, 460.0, "Ontario");
		System.out.println(city);
		System.out.println(city.getPopulation());
		get();
		
		dd();
	}

}
