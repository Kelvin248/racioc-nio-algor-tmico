import java.util.Scanner;
import java.util.ArrayList;

public class Repet5{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		
		ArrayList<Integer> list = new ArrayList<>();
		ArrayList<Integer> pares = new ArrayList<>();
		ArrayList<Integer> impares = new ArrayList<>();
		int count = 0;
		while (count <=10){
			System.out.println("numero:");
			int numero = scanner.nextInt();

			if (numero%2 == 0){
				pares.add(numero);
			}
			else{
				impares.add(numero);
			}
			count++;
		}
		System.out.println("pares:" + pares + "\nimpares:" + impares);
	}
}
