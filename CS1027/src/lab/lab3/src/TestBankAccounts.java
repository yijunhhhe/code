import java.io.*;

/**
 * TestBankAccounts.java:
 *  This class will test aspects of inheritance for the BankAccount class
 *  and its subclasses.
 * @author CS027b 2007
 */

public class TestBankAccounts {
    
    public static void main(String[] args) {
      
        BankAccount bacc0 = new BankAccount(0);
        System.out.println(bacc0.toString());
        
        BankAccount bacc1 = new BankAccount(5000);
        System.out.println(bacc1.toString());
        
        CheckingAccount chacc1 = new CheckingAccount(500.0);
        System.out.println(chacc1.toString());
                          
        SavingsAccount sacc1 = new SavingsAccount(1000.0, 1.0);
        
        System.out.println(sacc1.toString()); 
        
        //-------------------------------------------------------
        // add your code here
        
        //1  System.out.println(sacc1.toString()) and System.out.println(chacc1.toString()) is overriding
        
        bacc0 = chacc1;
        //2 This is legal because CheckingAccount is subclass of BankAccount
        
        System.out.println(bacc0.toString());
        //3 It uses CheckingAccount toString method
        
        //chacc1 = bacc1;
        //4 Illegal because subclass cannot reference its superclass
        
        BankAccount bacc2 = new CheckingAccount(200.0);
        chacc1 = (CheckingAccount) bacc2;
        //5 Illegal because chacc1 and bacc2 is different type of references
        	
        //bacc1.deductFees();
        chacc1.deductFees();
        //sacc1.deductFees();
        //6 CheckingAccount Object was legal because it has deductFees method
        
        //7 second and third step
        
        chacc1.deposit(100.0);
        //8 it throws an exception because it doesnt have super keyword to invoke the deposit method in bankaccount class
    }
    
}
