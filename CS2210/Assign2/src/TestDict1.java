

public class TestDict1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Dictionary dict = new Dictionary(9887);
			try {
			    dict.insert(new ConfigData("answer", 42));
			    System.out.println("   Test 1 succeeded");
			    dict.insert(new ConfigData("naswer", 38));
			    dict.insert(new ConfigData("werans", 42));
			    dict.insert(new ConfigData("ted", 42));
			    dict.insert(new ConfigData("det", 42));
			    dict.insert(new ConfigData("asd", 42));
			    dict.insert(new ConfigData("dsa", 42));
			    dict.insert(new ConfigData("qwe", 42));
			    
			    
			}
			catch (DictionaryException e) {
			    System.out.println("***Test 1 failed");
			}
			if (dict.find("answer") == -1) 
				System.out.println("***Test 3 failed");
			else System.out.println("   Test 3 succeeded");
		
	}
}
