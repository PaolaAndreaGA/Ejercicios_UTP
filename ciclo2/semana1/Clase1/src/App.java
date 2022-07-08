import java.util.Scanner;

public class App {
    private static int mynum;

    public static void main(String[] args) throws Exception {
        // ejercicio1();
        // ejercicio2();
        // ejercicio3();
        // ejercicio4();
        // ejercicio5();

        ejercicio6();

    }

    private static void ejercicio1() {
        var cadena = "Paola";
        System.out.printf("hola, %s, como va todo", cadena);
    }

    private static void ejercicio2() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        mynum = sc.nextInt();
        String number = String.valueOf(mynum);
        String[] digits = number.split("(?<=.)");
        int i;
        for (i = 0; i < digits.length; i++) {
        }
        sc.close();
        System.out.printf("el numero %d, es de %d cifras. \n", mynum, i);

    }

    private static void ejercicio3() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        int mynum = sc.nextInt();
        int numdob = mynum * 2;
        int numtri = mynum * 3;
        sc.close();
        System.out.printf("el doble del numero %d, es  %d. \n", mynum, numdob);
        System.out.printf("el triple del numero %d, es  %d. \n", mynum, numtri);

    }

    private static void ejercicio4() {

        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese temperatura en grados centigrados: ");
        mynum = sc.nextInt();
        int tempf = 32 + (9 * mynum / 5);
        System.out.printf("La temperatura en grados Fahrenheit es igual a: %d \n", tempf);
        sc.close();
    }

    private static void ejercicio5() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un numero ");
        mynum = sc.nextInt();
        if (mynum != 0) {
            System.out.printf("el %d " + ((mynum % 2 == 0) ? "par\n" : "es impar \n"), mynum);

        } else {
            System.out.printf("el numero %d es neutro \n", mynum);
        }
        sc.close();
    }

    /**
     * 
     */
    private static void ejercicio6() {
       
        Scanner operator = new Scanner(System.in);
        System.out.println("escoja una opcion: \n1. suma\n2. resta\n3. multipicacion\n4. division\n ");
        int operaciones = operator.nextInt();
        switch (operaciones) {
            case 1:
                System.out.println("Ingrese un numero ");
                Scanner sum1 = new Scanner(System.in);
                int mysum1 = sum1.nextInt();
                Scanner sum2 = new Scanner(System.in);
                System.out.println("Ingrese un numero ");
                int mysum2 = sum2.nextInt();
                int total = mysum1 + mysum2;
                System.out.println("el resultado de la suma es : " + total ); 
                sum1.close();
                sum2.close();
                break;
            case 2:
                System.out.println("Ingrese un numero ");
                Scanner res1 = new Scanner(System.in);
                int myres1 = res1.nextInt();
                Scanner res2 = new Scanner(System.in);
                System.out.println("Ingrese un numero ");
                int myres2 = res2.nextInt();
                int totalres = myres1 - myres2;
                System.out.println("el resultado de la resta es : " + totalres ); 
                res1.close();
                res2.close();
                break;
            case 3:
                System.out.println("Ingrese un numero ");
                Scanner mul1 = new Scanner(System.in);
                int mymul1 = mul1.nextInt();
                Scanner mul2 = new Scanner(System.in);
                System.out.println("Ingrese un numero ");
                int mymul2 = mul2.nextInt();
                int totalmul = mymul1 * mymul2;
                System.out.println("el resultado de la multiplicacion es : " + totalmul ); 
                mul1.close();
                mul2.close();
                break;
            case 4:
                System.out.println("Ingrese un numero ");
                Scanner div1 = new Scanner(System.in);
                int mydiv1 = div1.nextInt();
                Scanner div2 = new Scanner(System.in);
                System.out.println("Ingrese un numero ");
                int mydiv2 = div2.nextInt();
                int totaldiv = mydiv1 / mydiv2;
                System.out.println("el resultado de la division es :" + totaldiv ); 
                div1.close();
                div2.close();
                break;    
            default:
                
            System.out.println("Por favor digite una opcion valida de 1 a 4");
                break;               
        }
        operator.close();
    }
}
