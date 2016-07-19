/** Phone class
 *  represents a phone listing
 *  @author CS1027 for Lab
 */

public class Phone implements Comparable<Phone>{
  
  private String name;
  private String phone;
    
  public Phone(){
    name = "";
    phone = "";
  }
  public Phone(String name, String phone){
    this.name = name;
    this.phone = phone;
  }
  public String getName(){
    return name;
  }
  public String getPhone(){
    return phone;
  }
  public void setName(String name){
    this.name = name;
  }
  public void setPhone(String phone){
    this.phone = phone;
  }
  public String toString(){
    return (name + " " + phone);
  }
  public boolean equals(Phone other)
  {
	  return (name == other.name)&&(phone == other.phone);
	  
  }
  public int compareTo(Phone other) {
	// TODO Auto-generated method stub
	  
	  int compare = name.compareToIgnoreCase(other.getName());
	  if(compare > 0){
		  return 1;
	  } else if (compare == 0){
		  return 0;
	  } else {
		  return -1;
	  }
	  
	  /*int compare = phone.compareTo(other.getPhone());
	  if(compare > 0){
		  return 1;
	  } else if (compare == 0){
		  return 0;
	  } else {
		  return -1;
	
	  }*/
	  
  }
}


