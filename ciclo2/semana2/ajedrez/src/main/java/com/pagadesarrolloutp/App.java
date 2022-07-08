package com.pagadesarrolloutp;

import com.pagadesarrolloutp.modelo.Casilla;
import com.pagadesarrolloutp.modelo.Color;
import com.pagadesarrolloutp.modelo.Jugador;
import com.pagadesarrolloutp.modelo.tablero;

/**
 * Hello world!
 *
 */
public class App {
    public static void main(String[] args) {
        var paola = new Jugador();
        paola.nombre = "Paola";
        paola.color = Color.BLANCO;

        var leonardo = new Jugador();
        leonardo.nombre = "Leonardo";
        leonardo.color = Color.BLANCO;

        tablero.casillas = new Casilla[8][8];
        var tablero = new tablero();
        tablero.jugador1 = paola;
        tablero.jugador2 = leonardo;
        var casilla = new Casilla()
        casilla.color = Color.NEGRO;
        


    }
}
