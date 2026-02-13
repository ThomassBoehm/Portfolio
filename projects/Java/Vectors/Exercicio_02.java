import java.util.Arrays;

public class Exercicio_02 {
    public static void main(String[] args) {
        int tamanho = 100;
        int i;
        int[] vetor = new int[tamanho];

        for (i = 0; i < tamanho; i++) {
            if (i % 2 == 0) {
                vetor[i] = i+1;
            } 
            else {
                vetor[i] = 0;
            }
        }
        System.out.println(Arrays.toString(vetor));
    }
}
