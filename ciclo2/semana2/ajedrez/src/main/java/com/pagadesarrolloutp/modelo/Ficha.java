package com.pagadesarrolloutp.modelo;

public abstract class Ficha {
  private Color color;
  private Casilla origen;

public Ficha(Color color){
  this(color, origen:null);
}


public Ficha(Color color, Casilla casilla){
  
}

  public Boolean comer(){
    //TODO
    return true;
  }
  public abstract void mover(Casilla destino);

}
