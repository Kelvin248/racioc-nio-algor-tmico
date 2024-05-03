import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Repet9{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		ArrayList<Integer> lista = new ArrayList<>();

		for (int i = 0; i<=10; i++){
			System.out.println("digite o numero:");

			lista.add(scanner.nextInt());
		}
		Collections.sort(lista, Collections.reverseOrder());

		System.out.println(lista);
		
	}
}
