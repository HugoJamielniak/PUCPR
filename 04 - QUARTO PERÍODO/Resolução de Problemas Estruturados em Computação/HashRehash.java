import java.util.Random;

public class HashRehash {
    private int[] tabela;
    private int[] colisoes;
    private int tamanho;
    private int ocupacao;
    private int totalColisoes;

    public HashRehash(int tamanho) {
        this.tamanho = tamanho;
        this.tabela = new int[tamanho];
        this.colisoes = new int[tamanho];

        for (int i = 0; i < tamanho; i++) {
            tabela[i] = -1;
        }
    }

    public int hash(int elemento) {
        return elemento % tamanho;
    }

    public boolean inserir(int elemento) {
        if (ocupacao >= tamanho * 90 / 100) {
            return false;
        }
        int posicao = hash(elemento);
        int contador = 0;

        while (tabela[posicao] != -1) {
            contador++;
            posicao = (posicao + 1) % tamanho;
        }
        tabela[posicao] = elemento;
        colisoes[posicao] = contador;
        totalColisoes += contador;
        ocupacao++;
        return true;
    }

    public boolean buscar(int elemento) {
        int posicao = hash(elemento);
        while (tabela[posicao] != -1) {
            if (tabela[posicao] == elemento) {
                return true;
            }
            posicao = (posicao + 1) % tamanho;
        }
        return false;
    }

    public void imprimirResultados() {
        System.out.println("Total de colisoes: " + totalColisoes);
        System.out.println("Posicoes livres:");
        for (int i = 0; i < tamanho; i++) {
            if (tabela[i] == -1) {
                System.out.println(i);
            }
        }
        int[] top = new int[3];
        boolean[] escolhido = new boolean[tamanho];

        for (int k = 0; k < 3; k++) {
            int melhor = -1;
            for (int i = 0; i < tamanho; i++) {
                if (tabela[i] != -1 && !escolhido[i]) {
                    if (melhor == -1 || colisoes[i] > colisoes[melhor]) {
                        melhor = i;
                    }
                }
            }
            escolhido[melhor] = true;
            top[k] = melhor;
        }
        System.out.println("Tres elementos que mais colidiram:");
        for (int k = 0; k < 3; k++) {
            System.out.println(tabela[top[k]] + " - " + colisoes[top[k]] + " colisoes");
        }
        System.out.println("Teste de busca:");
        for (int k = 0; k < 3; k++) {
            System.out.println(tabela[top[k]] + ": " + buscar(tabela[top[k]]));
        }
    }
    public static void main(String[] args) {
        HashRehash hash = new HashRehash(100);
        Random random = new Random(1090);
        for (int i = 0; i < 100; i++) {
            int valor = random.nextInt(100001);
            hash.inserir(valor);
        }

        hash.imprimirResultados();
    }
}
