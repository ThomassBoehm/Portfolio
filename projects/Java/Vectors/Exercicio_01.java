import java.util.Arrays;
public class Exercicio_01 {
    public static void main(String[] args) {
        int tamanho = 100;
        int i;
        int[] vetor = new int[tamanho];

        // Laço for
        for (i = 0; i < tamanho; i++) {
            vetor[i] = 0;
    }
        // Laço while
        i = 0;
        while (i < tamanho) {
            vetor[i] = 0;
            i++;
        }

        // Laço do-while
        i = 0;
        if (vetor.length > 0) {
        do {
            vetor[i] = 0;
            i++;
            } while (i < tamanho);
         }
         System.out.println(Arrays.toString(vetor));
    }
}