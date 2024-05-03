import java.util.ArrayList;
import java.util.Scanner;

public class Repet4{
	public static void main(String[] args){
		ArrayList<Integer> list = new ArrayList<>();
		Scanner scanner = new Scanner(System.in);
		
		int idade = 0;

		while (true){
		System.out.println("Digite idade em anos (0 para sair):");
		int anos = scanner.nextInt();


		if (anos > 0){
			list.add(anos);
			 idade += anos;

		}
		else if (anos == 0){
			break;
		}
		}
		int sizeList = list.size();
		System.out.println("Média:"+ idade/ sizeList);

	
}
}
