public class SavingsAccount extends BankAccount {
	private double interestRate;
	
	
	
	public SavingsAccount(double initialAmount, double rate) {
		// TODO Auto-generated constructor stub
		super(initialAmount);
		interestRate = rate;
	}



	public double getInterestRate(){
		return interestRate;
	}
	
	public void calculateInterest(){
		balance = balance + balance * interestRate;		
	}
	
	public String toString(){
		return ("SavingsAccount: " + "balance: " + balance + ", Interest Rate: " + interestRate);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	}
	
	
}
