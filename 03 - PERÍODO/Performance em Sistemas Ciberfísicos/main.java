import java.io.*;
import java.util.HashMap;

class ThreadContarLetras extends Thread {
    private File[] arquivos;
    private int inicio, fim;
    private HashMap<Character, Integer> contadorParcial = new HashMap<>();

    public ThreadContarLetras(File[] arquivos, int inicio, int fim) {
        this.arquivos = arquivos;
        this.inicio = inicio;
        this.fim = fim;
    }

    public void run() {
        for (int i = inicio; i < fim; i++) {
            try (BufferedReader br = new BufferedReader(new FileReader(arquivos[i]))) {
                String linha;
                while ((linha = br.readLine()) != null) {
                    for (int j = 0; j < linha.length(); j++) {
                        char letra = linha.charAt(j);
                        if (Character.isLetter(letra)) {
                            contadorParcial.put(letra, contadorParcial.getOrDefault(letra, 0) + 1);
                        }
                    }
                }
            } catch (IOException e) {
                System.err.println("Erro ao ler arquivo: " + arquivos[i].getName());
            }
        }
    }

    public HashMap<Character, Integer> getContadorParcial() {
        return contadorParcial;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        long inicioTempo = System.currentTimeMillis();
        File pasta = new File("todosArquivos");
        File[] lista = pasta.listFiles();

        if (lista == null || lista.length == 0) return;

        int total = lista.length;
        int d = total / 4;


        ThreadContarLetras t1 = new ThreadContarLetras(lista, 0, d);
        ThreadContarLetras t2 = new ThreadContarLetras(lista, d, 2 * d);
        ThreadContarLetras t3 = new ThreadContarLetras(lista, 2 * d, 3 * d);
        ThreadContarLetras t4 = new ThreadContarLetras(lista, 3 * d, total);

        t1.start();
        t2.start();
        t3.start();
        t4.start();

        t1.join();
        t2.join();
        t3.join();
        t4.join();


        HashMap<Character, Integer> totalLetras = new HashMap<>();
        ThreadContarLetras[] threads = {t1, t2, t3, t4};

        for (ThreadContarLetras t : threads) {
            t.getContadorParcial().forEach((l, q) ->
                    totalLetras.put(l, totalLetras.getOrDefault(l, 0) + q));
        }

        long tempoExecucao = System.currentTimeMillis() - inicioTempo;

        totalLetras.forEach((l, q) -> System.out.println(l + ": " + q));
        System.out.println("\nTempo de execução: " + tempoExecucao + " ms");
    }
}
