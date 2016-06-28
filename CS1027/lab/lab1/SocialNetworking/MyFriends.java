public class MyFriends {
  public static void main(String args[]) {

    SocialNetwork contacts = new SocialNetwork();

    contacts.add("Snoopy","Dog","snoopy@uwo.ca");
    contacts.add("Felix","Cat","felix@uwo.ca");
    contacts.add("Mickey","Mouse","mickey@uwo.ca");
    contacts.remove("Snoopy", "Dog");
    System.out.println("Snoopy Dog was removed successfully");
    contacts.remove("Yijun", "He");
    System.out.println("Yijun He was not in the lists");
    
  

    System.out.println(contacts.toString());
    //System.out.println("I have " + contacts.getNumFriends() + " friends in my list.");
  }
}
