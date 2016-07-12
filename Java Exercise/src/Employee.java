
public class Employee {
	String name;          // Name of the employee.
	   
	   Employee supervisor;  // The employee's supervisor.
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Employee emp = new Employee();
		if ( emp.supervisor == null) {
			   System.out.println( emp.name + " is the boss and has no supervisor!" );
			}
			else {
			   System.out.print( "The supervisor of " + emp.name + " is " );
			   System.out.println( emp.supervisor.name );
			}
		
		if ( emp.supervisor == null ) {
			   System.out.println( emp.name + " is the boss!" );
			}
			else {
			   Employee runner;  // For "running" up the chain of command.
			   runner = emp.supervisor;
			   if ( runner.supervisor == null) {
			      System.out.println( emp.name  + " reports directly to the boss." );
			   }
			   else {
			      int count = 0;
			      while ( runner.supervisor != null ) {
			         count++;  // Count the supervisor on this level.
			         runner = runner.supervisor; // Move up to the next level.
			      }
			      System.out.println( "There are " + count
			                             + " supervisors between " + emp.name
			                             + " and the boss." );
			   }
			}
	}
}
