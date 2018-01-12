package Lab6;

public class BadTransactionException extends Exception {
int transactenumber;
public BadTransactionException(int n){
	super("the bad transactenumber is "+n);
	this.transactenumber=n;
}
}
