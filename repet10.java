import java.util.*;


public class Repet10{
	public static void main(String[] args){
		ArrayList<Integer> lista = new ArrayList<>(Arrays.asList(2,4,7,2,3,3,1,0,2,6));

		int freq = 0;
		int freq_old = 0;
		int num = 0;
		
		for(int count = 0;count < lista.size(); count++){
			for (int i =0 ; i< lista.size(); i++){
				if(lista.get(count) == lista.get(i)){
					freq += 1;
				
					if (freq < freq_old){
						freq = freq_old;
					}
					else{
						num = lista.get(count);
					}
				}
					
			}
				freq_old = freq;
				freq = 0;
				
		}

		System.out.println("O numero que mais aparece é:" +num);	

	}
}

