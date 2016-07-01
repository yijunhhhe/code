public class SavingsAccount extends BankAccount {
	private double interestRate;
	// if interest rate is fix
	// private final interestRate = 0.5;
	
	public SavingsAccount(double initialAmount, double rate) {
		// TODO Auto-generated constructor stub
		super(initialAmount);
		interestRate = rate;
	}



	public double getInterestRate(){
		return interestRate;
	}
	
	public void calculateInterest(){
		balance = balance + balance * interestRate/100;		
	}
	
	public String toString(){
		return ("SavingsAccount: " + "balance: $" + balance + ", Interest Rate: " + interestRate);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}
	
	
}
