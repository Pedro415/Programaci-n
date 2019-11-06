#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:15:04 2019

@author: hipatia
"""


#aqui se muestra el codigo para la resolucion de la parte de la tasa 
def GetValorDeCuota(monto, tasa, cuotas, periodo="mensual"):
     #Retorna el valor actual de la cuota, según el  en donde las cuotas son fijas.                     
     #Formula = R = P [(i (1 + i)**n) / ((1 + i)**n – 1)].     
     #        R = renta (cuota)         
     #       P = principal (préstamo adquirido)         
     #       i = tasa de interés         
     #       n = número de periodos         
    tasa = tasa / 100.0             
    if periodo == "diario":         
        tasa /= 30.4167     
    elif periodo == "semanal":         
        tasa /= 4.34524     
    elif periodo == "quincenal":         
        tasa /= 2.0     
    elif periodo == "bimestral":         
        tasa *= 2     
    elif periodo == "trimestral":         
        tasa *= 3     
    elif periodo == "cuatrimestral":         
        tasa *= 4    
    elif periodo == "semestral":         
        tasa *= 6     
    elif periodo == "anual":         
        tasa *= 12             
    return monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) ) 