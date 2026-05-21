import java.util.Random;

class Conta {
    private double valor;
    public Conta(){this.valor=0;}
    public void Deposito(double valor){
        this.valor += valor;
        System.out.println("Deposito realizado");
        System.out.println("Saldo atual: " + Saldo());
    }
    public void Saque(double valor){
        if(this.valor > valor){
            this.valor -= valor;
            System.out.println("Saque realizado");
            System.out.println("Saldo atual: " + Saldo());
        }
        else{
            System.out.println("Saldo insuficiente");
            System.out.println("Saldo atual: " + Saldo());
        }
    }
    public double Saldo(){return this.valor;}
}

class Depositos extends Thread{
    private Conta Depositos;
    Random gerador = new Random();
    public Depositos(Conta Depositos){this.Depositos= Depositos;}
    public void run(){
        double valor = gerador.nextInt(100);
        while(true){ synchronized (this.Depositos){
            this.Depositos.Deposito(valor);
        }
            try{
                Thread.sleep(100);
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}

class Saques extends Thread{
    private Conta Saques;
    Random gerador = new Random();
    public Saques(Conta Saques){this.Saques= Saques;}
    public void run(){
        while(true){
            double valor = gerador.nextInt(100);
            synchronized (this.Saques) {
                this.Saques.Saque(valor);
            }
            try{
                Thread.sleep(100);
            }
            catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}

public class Main {

    public static void main(String[] args) throws InterruptedException {

        Conta conta = new Conta();

        Depositos minhaThread1 = new Depositos(conta);
        Depositos minhaThread2 = new Depositos(conta);

        Saques minhaThread3 = new Saques(conta);
        Saques minhaThread4 = new Saques(conta);
        Saques minhaThread5 = new Saques(conta);

        minhaThread1.start();
        minhaThread2.start();

        minhaThread3.start();
        minhaThread4.start();
        minhaThread5.start();

        minhaThread1.join();
        minhaThread2.join();

        minhaThread3.join();
        minhaThread4.join();
        minhaThread5.join();
    }
}