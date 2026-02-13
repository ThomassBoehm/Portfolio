public class Exercicio_06 {
    public static void main(String[] args) {
        final int linhas = 5;
        final int colunas = 5;
        int[][] matriz = new int[linhas][colunas];

        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                matriz[i][j] = (i + 1) * (j + 1);
            }
        }
        System.out.println("Matriz preenchida:");
        // Imprimir a matriz
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println(); // Nova linha após cada linha da matriz
        }

        //limpar matriz
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                matriz[i][j] = -1;
            }
        }
        System.out.println("Matriz limpa:");
        // Imprimir a matriz
        for (int i = 0; i < linhas; i++) {
            for (int j = 0; j < colunas; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println(); // Nova linha após cada linha da matriz
        }

    }
}
