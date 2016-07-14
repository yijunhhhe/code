
public class Random {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer a = new Integer(4);
		Integer b = new Integer(5);
		String s = new String("yes");
		
		System.out.println(a.equals(b));
		int c = a.intValue();
		double d = a.doubleValue();
		String suck = a.toString();
		int e = Integer.parseInt("5");
		
		String string = "what the fuck";
		int index = string.indexOf("a");
		int index1 = string.indexOf(2);
		System.out.println(index1);
		int lastIndex = string.lastIndexOf("h");
		System.out.println(lastIndex);
		System.out.println(index);
		System.out.println(string.substring(5));
		System.out.println(string.substring(3, 6));
		
		StringBuffer aaa = new StringBuffer("suck");
		aaa.insert(2, "what");
		aaa.append(4);
		System.out.println(aaa.length());
		aaa.setCharAt(1, 'a');
		String bbb = aaa.toString();
		StringBuffer ccc = aaa.reverse();
		aaa.delete(4, 6);
		aaa.replace(5,5,"a");
		System.out.println(aaa);
	}

}
