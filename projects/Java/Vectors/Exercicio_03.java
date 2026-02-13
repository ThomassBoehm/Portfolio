import java.util.Arrays;

public class Exercicio_03 {
    public static void main(String[] args) {
        char[] vetor = new char[26];
        char letra = 'A';
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = letra;
            letra++;
        }
        System.out.println(Arrays.toString(vetor));
    }
}