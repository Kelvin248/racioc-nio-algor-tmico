import java.util.Scanner;
import java.util.ArrayList;

public class Repet8{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		ArrayList<Integer> divisores = new ArrayList<>();
		
		int num = 0;
		while (true){
		System.out.println("digite o numero positivo não nulo:");
		
		int numero = scanner.nextInt();
		num = numero;

		if (numero<= 0){
			System.out.println("ERROR");
		}
		else{
			for (int i=1; i<= numero; i++){
				if (numero%i == 0){
					divisores.add(i);
				}

			}
			break;
		}
	}
	System.out.println("Os disores de " + num + " São:");
	System.out.println(divisores);
}
}
