import java.util.*;

class collatz {

	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number");
		int n=sc.nextInt();
		System.out.println("The Collatz Sequence for the given number is as follows:");
		System.out.print(n+" ");
		while(n!=1)
		{
			
			if(n%2==0)
				n=n/2;
			else
				n=3*n+1;
			System.out.print(n+" ");
		}
		
		
	}
}
