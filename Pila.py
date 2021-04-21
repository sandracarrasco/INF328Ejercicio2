# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 22:54:08 2021

@author: sady2
"""

class Pila:
  def __init__(self):
      self.elementos = []
  def apilar(self,a):
      self.elementos.append(a)
  def desapilar(self):
      if self.estaVacia():
          print("La pila esta vacia")
          return None
      return self.elementos.pop()
  def imprimir(self):
      print(self.elementos)
  def tamaño(self):
      return len(self.elementos)
  def estaVacia(self):
      return len(self.elementos)==0
  def limpiar(self):
      del self.elementos[:]
  def cima(self):
      if self.estaVacia():
          print("La pila esta vacia")
          return None
      return self.elementos[-1]
  def inspeccionar(self):
      return self.elementos[len(self.elementos)-1]