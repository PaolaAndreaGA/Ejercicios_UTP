package com.pagadesarrolloutp.modelo;

public class Casilla {
  public Integer fila;    
  public Character columna;
  public Color color;

  public Ficha ficha; 

  public Boolean estaOcupada(){
    if (ficha != null){
      return true;
    }
    return false;
  }
}
