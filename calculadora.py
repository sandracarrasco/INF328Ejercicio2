# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 12:13:29 2021

@author: sady2
"""

from tkinter import *
import parser
from Pila import Pila
ventana= Tk()
ventana.title("Calculadora inf 328")

#etiqueta = Label(ventana,text = "ejemplo 328")
#etiqueta.grid(column=0,row=6)
txt=Entry(ventana,width=15)
txt.grid(columnspan=6,row=1,sticky=W+E)
i=0
def obtenerNumeros(numero):
   global i
   txt.insert(i,numero)
   i=i+1

   
def limpiar():
    txt.delete(0,END)
def valor():
    estado=txt.get() 
    etiqueta.configure(text= estado)
    
def calcular():
    estado=txt.get() 
    print(estado)
    try:
        resultado = infija_a_posfija(estado)
       # expresion = parser.expr(estado).compile()
        #resultado = eval(expresion)
        resultado=evaluar(resultado)
        limpiar()
        txt.insert(0,resultado)
    except expression as identifier :
        pass
    
def infija_a_posfija(expresionInfija):
    expresionInfija = list(expresionInfija.upper())
    print (expresionInfija)
    listaSimbolos=expresionInfija
    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1
    pilaOperadores = Pila()
    listaSufija = []
   #listaSimbolos = expresionInfija.split()
    print(listaSimbolos)

    for simbolo in listaSimbolos:
        if simbolo in "0123456789":
            listaSufija.append(simbolo)
        elif simbolo == '(':
            pilaOperadores.apilar(simbolo)
        elif simbolo == ')':
            simboloTope = pilaOperadores.desapilar()
            while simboloTope != '(':
                listaSufija.append(simboloTope)
                simboloTope = pilaOperadores.desapilar()
        else:
            while (not pilaOperadores.estaVacia()) and \
               (precedencia[pilaOperadores.inspeccionar()] >= \
                precedencia[simbolo]):
                  listaSufija.append(pilaOperadores.desapilar())
            pilaOperadores.apilar(simbolo)

    while not pilaOperadores.estaVacia():
        listaSufija.append(pilaOperadores.desapilar())
    return " ".join(listaSufija)

def evaluar(resultado):
    pilaOperadores = Pila()
    listaSufija = []
    resultado = list(resultado.upper())
    print (resultado)
    
    for simbolo in resultado:
        if simbolo in "0123456789":
            pilaOperadores.apilar(simbolo)
        else: 
            if simbolo in "+-*/":
               simboloTope2= pilaOperadores.desapilar()
               simboloTope = pilaOperadores.desapilar()
               
               res= calcularO(simboloTope,simbolo,simboloTope2)
               pilaOperadores.apilar(res)
    while not pilaOperadores.estaVacia():
       listaSufija.append(pilaOperadores.desapilar())
    return " ".join(listaSufija)
    
def calcularO(a,b,c):
    a=int(a)
    c=int(c)
    res=0
    if b=='+' :
       res=a+c
       res=str(res)
       return res
       
    if b=='-' :
       res=a-c
       res=str(res)
       return res
    if b=='*' :
       res=a*c
       res=str(res)
       return res
    if b=='/' :
       res=a/c
       res=str(res)
       return res
#Numeros
Button(ventana,text="1",command=lambda:obtenerNumeros(1)).grid(row=2,column=0)
Button(ventana,text="2",command=lambda:obtenerNumeros(2)).grid(row=2,column=1)
Button(ventana,text="3",command=lambda:obtenerNumeros(3)).grid(row=2,column=2)

Button(ventana,text="4",command=lambda:obtenerNumeros(4)).grid(row=3,column=0)
Button(ventana,text="5",command=lambda:obtenerNumeros(5)).grid(row=3,column=1)
Button(ventana,text="6",command=lambda:obtenerNumeros(6)).grid(row=3,column=2)

Button(ventana,text="7",command=lambda:obtenerNumeros(7)).grid(row=4,column=0)
Button(ventana,text="8",command=lambda:obtenerNumeros(8)).grid(row=4,column=1)
Button(ventana,text="9",command=lambda:obtenerNumeros(9)).grid(row=4,column=2)

Button(ventana,text="0",command=lambda:obtenerNumeros(0)).grid(row=5,column=1)

#operaciones
Button(ventana,text="+",command=lambda:obtenerNumeros("+")).grid(row=2,column=3)
Button(ventana,text="-",command=lambda:obtenerNumeros("-")).grid(row=3,column=3)
Button(ventana,text="*",command=lambda:obtenerNumeros("*")).grid(row=4,column=3)
Button(ventana,text="/",command=lambda:obtenerNumeros("/")).grid(row=5,column=3)

Button(ventana,text="(",command=lambda:obtenerNumeros("(")).grid(row=3,column=4,sticky=W+E)
Button(ventana,text=")",command=lambda:obtenerNumeros(")")).grid(row=4,column=4,sticky=W+E)

Button(ventana,text="=",command=lambda:calcular()).grid(row=5,column=4)
Button(ventana,text="AC",command=lambda:limpiar()).grid(row=2,column=4)


ventana.mainloop()  
