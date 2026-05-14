        double[] numeros = new double[2_000_000];


        ThreadPreencher p1 = new ThreadPreencher(numeros, 0, 500_000);
        ThreadPreencher p2 = new ThreadPreencher(numeros, 500_000, 1_000_000);
        ThreadPreencher p3 = new ThreadPreencher(numeros, 1_000_000, 1_500_000);
        ThreadPreencher p4 = new ThreadPreencher(numeros, 1_500_000, 2_000_000);

        p1.start();
        p2.start();
        p3.start();
        p4.start();

        p1.join();
        p2.join();
        p3.join();
        p4.join();
        System.out.println("Encerrou a inicialização");

        ThreadContar c1 = new ThreadContar(numeros, 0, 500_000);
        ThreadContar c2 = new ThreadContar(numeros, 500_000, 1_000_000);
        ThreadContar c3 = new ThreadContar(numeros, 1_000_000, 1_500_000);
        ThreadContar c4 = new ThreadContar(numeros, 1_500_000, 2_000_000);

        c1.start();
        c2.start();
        c3.start();
        c4.start();

        c1.join();
        c2.join();
        c3.join();
        c4.join();

        int totalCriterio = c1.getContadorParcial() + c2.getContadorParcial() + c3.getContadorParcial() + c4.getContadorParcial();

        System.out.println("Total de números entre 0.25 e 0.75: " + totalCriterio);
