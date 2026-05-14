import java.util.Random;

class ThreadPreencher extends Thread {
    private double[] numeros;
    private int inicio, fim;

    public ThreadPreencher(double[] numeros, int inicio, int fim) {
        this.numeros = numeros;
        this.inicio = inicio;
        this.fim = fim;
    }

    public void run() {
        Random random = new Random();
        for (int i = inicio; i < fim; i++) {
            numeros[i] = random.nextDouble();
        }
    }
}

class ThreadContar extends Thread {
    private double[] numeros;
    private int inicio, fim;
    private int contadorParcial = 0;

    public ThreadContar(double[] numeros, int inicio, int fim) {
        this.numeros = numeros;
        this.inicio = inicio;
        this.fim = fim;
    }

    public void run() {
        for (int i = inicio; i < fim; i++) {
            if (numeros[i] > 0.25 && numeros[i] < 0.75) {
                contadorParcial++;
            }
        }
    }

    public int getContadorParcial() {
        return contadorParcial;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        double[] numeros = new double[2_000_000];


        ThreadPreencher p1 = new ThreadPreencher(numeros, 0, 1_000_000);
        ThreadPreencher p2 = new ThreadPreencher(numeros, 1_000_000, 2_000_000);
        

        p1.start();
        p2.start();

        p1.join();
        p2.join();
       
        System.out.println("Encerrou a inicialização");

        ThreadContar c1 = new ThreadContar(numeros, 0, 1_000_000);
        ThreadContar c2 = new ThreadContar(numeros, 1_000_000, 2_000_000);
    

        c1.start();
        c2.start();

        c1.join();
        c2.join();

        int totalCriterio = c1.getContadorParcial() + c2.getContadorParcial();

        System.out.println("Total de números entre 0.25 e 0.75: " + totalCriterio);
    }
}
