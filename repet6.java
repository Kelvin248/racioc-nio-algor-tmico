import java.util.Scanner;
import java.util.ArrayList;

public class Repet6{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		
		ArrayList<Integer> dentro = new ArrayList<>();
		ArrayList<Integer> fora = new ArrayList<>();

		for (int count = 0; count <= 10; count++){
			System.out.println("digite o valor:");
			int valor = scanner.nextInt();

			if(valor >= 10 && valor <=20){

				dentro.add(valor);
			}
			else{
				fora.add(valor);
			}

		}
		scanner.close();

		System.out.println("valores entre {10,20}:" + dentro + "\nfora disso:" + fora);
	}
}
