import java.util.Scanner; 


public class Exercicio_05 {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);
        int vetor[] = new int[16];
        int capicuas = 0;

        System.out.println("Digite 16 numeros inteiros:");
        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Indice " + i + ": ");
            vetor[i] = leitor.nextInt();
        }

        // 2. O limite i < 13 garante que i+3 chegue até 15 (o último índice)
        for (int i = 0; i < 13; i++) {
            if (vetor[i] == vetor[i + 3] && vetor[i + 1] == vetor[i + 2]) {
                capicuas++;
                System.out.println("Capicua encontrada: " + vetor[i] + " " + vetor[i + 1] + " " + vetor[i + 2] + " " + vetor[i + 3] + " nos Índices: " + i + " a " + (i + 3));
            }
        }
        
        System.out.println("Total de capicuas encontradas: " + capicuas);
        leitor.close(); // Boa prática: fechar o scanner
    }
}