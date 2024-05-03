import java.util.Scanner;

public class repet2{
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);

		while (true){
		System.out.print("Numero(1,10):");
		int number = scanner.nextInt();
		
		if (number < 1 || number > 10){
			System.out.println("ERROR");
		}
		
		else{
			for (int i=0;i<=10;i++){
				System.out.print(number + "x" + i + "=" +number*i + "\n");
			}
			break;
			}

		}
		scanner.close();
	}
}
