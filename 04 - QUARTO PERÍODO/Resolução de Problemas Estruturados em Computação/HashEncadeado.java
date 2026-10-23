import java.util.Random;

public class HashEncadeado {
    class No {
        int elemento;
        No proximo;

        No(int elemento) {
            this.elemento = elemento;
        }
    }

    No[] tabela;
    int tamanho;

    public HashEncadeado(int tamanho) {
        this.tamanho = tamanho;
        this.tabela = new No[tamanho];
    }

    public int hash(int elemento) {
        return elemento % tamanho;
    }

    public boolean inserir(int elemento) {
        int i = hash(elemento);
        No novo = new No(elemento);
        boolean colisao = tabela[i] != null;
        novo.proximo = tabela[i];
        tabela[i] = novo;

        return colisao;
    }

    public int tamanhoLista(int i) {
        int contador = 0;
        No atual = tabela[i];
        while (atual != null) {
            contador++;
            atual = atual.proximo;
        }
        return contador;
    }

    public void imprimirResultados(int[] tresUltimos) {
        int maior = 0;
        int posicaoMaior = -1;
        int listasEncadeadas = 0;
        int vazias = 0;
        for (int i = 0; i < tamanho; i++) {
            int quantidade = tamanhoLista(i);
            if (quantidade == 0) {
                vazias++;
            } else {
                if (quantidade > 1) {
                    listasEncadeadas++;
                }
                if (quantidade > maior) {
                    maior = quantidade;
                    posicaoMaior = i;
                }
            }
        }

        System.out.println("Maior lista encadeada (posicao " + posicaoMaior + ", " + maior + " elementos):");
        No atual = tabela[posicaoMaior];

        while (atual != null) {
            System.out.print(atual.elemento + " -> ");
            atual = atual.proximo;
        }
        System.out.println("null");
        System.out.println("Listas encadeadas geradas: " + listasEncadeadas);
        System.out.println("Posicoes vazias: " + vazias);
        System.out.println("Tres ultimos valores inseridos em listas encadeadas:");

        for (int i = 0; i < 3; i++) {
            System.out.println(tresUltimos[i]);
        }
    }

    public static void main(String[] args) {
        HashEncadeado hash = new HashEncadeado(100);
        Random random = new Random(1090);

        int[] tresUltimos = new int[3];

        for (int i = 0; i < 1000; i++) {
            int valor = random.nextInt(100001);
            if (hash.inserir(valor)) {
                tresUltimos[0] = tresUltimos[1];
                tresUltimos[1] = tresUltimos[2];
                tresUltimos[2] = valor;
            }
        }
        hash.imprimirResultados(tresUltimos);
    }
}
