import java.util.Arrays;

public class Exercicio_04 {
    public static void main(String[] args) {
        char[] vetor = new char[26];
        char letra = 'A';
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = letra;
            letra++;
        }
        
        for (int n = 0; n < vetor.length; n++) {
            if (n % 2 == 0) {
                char temp = vetor[n]; 
                vetor[n] = vetor[n+1];
                vetor[n+1] = temp;
            }
        }
        System.out.println(Arrays.toString(vetor));
    }
}