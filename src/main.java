import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int Tab[][] = new int [14][14];
		int i;
		int[] inic= {1,1};
		int contador =0;
		ArrayList<int[]> Usados = new  ArrayList<int[]>();
		for (int j=0; j<14;j++){
			for (int k=0; k<14;k++){
				Tab[k][j]=0;
			}
		}
		for (i=0;i<14;i++){
			Tab[i][0] = 1;
			Tab[0][i] = 1;
			Tab[13][i] = 1;
			Tab[i][13] = 1;
		}
		for (int[] x : Tab){
			for (int z : x){
				System.out.print(z);
				System.out.print('\t');
			}
			System.out.println();
		}
		System.out.println();
		System.out.println();
		Usados.add(inic);
		while(contador<15){
			int[][] novolocal = new int[15][2];
			Random geradorrandom = new Random();
			int posX = geradorrandom.nextInt(12)+1;
			int posY = geradorrandom.nextInt(12)+1;
			novolocal[contador][0] = posX;
			novolocal[contador][1] = posY;
			if(!Usados.contains(novolocal)){
				contador++;
				Tab[posX][posY] = 200;
				//Usados.add(novolocal);
			}else{
				System.out.println("Uma hora rodando tinha que entrar aqui");
			}
		}
		for (int[] x : Tab){
			for (int z : x){
				System.out.print(z);
				System.out.print('\t');
			}
			System.out.println();
		}
		Integracao_Prolog teste = new Integracao_Prolog();

	}

}
