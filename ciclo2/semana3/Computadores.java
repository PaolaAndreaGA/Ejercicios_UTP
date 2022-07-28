public class Computadores {
  // Variables base
  // Variables
  // Constructores public Computadores(){
  // Constructor
  public Computadores() {
  }

  public Computadores(Double precioBase, Integer peso) {
  }

  public Computadores(Double precioBase, Integer peso, char consumoW) {
    this.precioBase = precioBase;
    this.peso = peso;
    this.consumoW = consumoW;
  }

  // Metodos
  public Double calcularPrecio(char consumoW, Integer peso) {
    Double adicion = 0.0;
    if (consumoW == 'A') {
      return adicion = 100.0;
    } else if (consumoW == 'B') {
      return adicion = 80.0;
    } else if (consumoW == 'C') {
      return adicion = 60.0;
    } else if (consumoW == 'D') {
      return adicion = 50.0;
    } else if (consumoW == 'E') {
      return adicion = 30.0;
    } else if (consumoW == 'F') {
      return adicion = 10.0;
    }

    if ((peso >= 0) & (peso < 19)) {
      return adicion + 10.0;
    } else if ((peso >= 20) & (peso < 49)) {
      return adicion + 50.0;
    } else if ((peso >= 50) & (peso < 79)) {
      return adicion + 80.0;
    } else if (peso >= 80) {
      return adicion + 100.0;
    } else {
      return adicion = 0.0;
    }

  }

  // Getter
  public class ComputadoresMesa extends Computadores {
    private final static Integer ALMACENAMIENTO_BASE = 50;

    // Variable
    // Constructor
    public ComputadoresMesa() {
    }

    // Constructor
    public ComputadoresMesa(Double precioBase, Integer peso) {
    }

    // Constructor
    public ComputadoresMesa(Double precioBase, Integer peso, char consumoW, Integer almacenamiento) {
    }

    // Métodos
    public Double calcularPrecio(Double adicion, Integer almacenamiento) {
      // Código return adicion;
      almacenamiento = ALMACENAMIENTO_BASE;
      if (almacenamiento > 100) {
        return adicion + 50.0;
      } else {
        return adicion;
      }
    }

    public Integer getCarga(Integer almacenamiento) {
      return almacenamiento;
    }
  }

  public class ComputadoresPortatiles extends Computadores {
    private final static Integer PULGADAS_BASE = 20;
    private Integer pulgadas;
    private boolean camaraITG;

    // Constructor
    public ComputadoresPortatiles() {
    }

    // Constructor
    public ComputadoresPortatiles(Double precioBase, Integer peso) {
    }

    // Constructor
    public ComputadoresPortatiles(Double precioBase, Integer peso, char consumoW, Integer pulgadas,
        boolean camaraITG) {
    }

    // Métodos
    public Double calcularPrecio(Double adicion, Double precioBase) {
      // Método Código return adicion;
      if (pulgadas > 40) {
        adicion = adicion + (precioBase * 0.3);
        if (camaraITG == true) {
          adicion = adicion + (precioBase * 0.5);
        }
        return adicion;
      } else {
        return adicion;
      }
    }
  }

  public class PrecioTotal {
    private Double totalComputadores = 0.0;
    private Double totalComputadoresPortatiles = 0.0;
    private Double totalComputadoresMesa = 0.0;
    private Computadores[] listaComputadores;

    // Constructor
    PrecioTotal(Computadores[] pComputadores) {
      this.listaComputadores = pComputadores;
    }

    public void mostrarTotales() {
      // Código
      // Mostramos los resultados
      System.out.println("La suma del precio de los computadores es de " + totalComputadores);
      System.out.println("La suma del precio de los computadores de mesa es de " + totalComputador);
      System.out.print("La suma del precio de los computadores portátiles es de " + totalComputadoresPortatiles);
    }
  }
}

public class Main {
public static void main(String[] args) {
// Pruebas Públicas
Computadores computadores[] = new Computadores[6];
computadores[0] = new Computadores(150.0, 70, 'A');
computadores[1] = new ComputadoresMesa(70.0, 40);
computadores[2] = new ComputadoresPortatiles(600.0, 70, 'D', 50, false);
computadores[3] = new Computadores();
computadores[4] = new Computadores(500.0, 60, 'A');
computadores[5] = new Computadores(700.0, 50, 'D');
PrecioTotal solucion1 = new PrecioTotal(computadores);
solucion1.mostrarTotales();
System.out.println();
Computadores computadores[] = new Computadores[4];
computadores[0] = new Computadores(60.0, 10, 'D');
computadores[1] = new ComputadoresMesa(300.0, 40, 'Z', 40);
computadores[2] = new ComputadoresPortatiles(50.0, 10, 'A', 70, false);
computadores[3] = new Computadores(50.0, 10);
PrecioTotal solucion1 = new PrecioTotal(computadores);
solucion1.mostrarTotales();
System.out.println()
}
}