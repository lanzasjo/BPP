import pytest
import Practica_L2_Jose_Lanzas
import pandas as pd


# Damos un DataFrame sencillo para hacer el testeo
lista = [[1,-2,3],[-4,5,-6],[7,-8,9]]

df = pd.DataFrame(lista, columns=['Enero','Febrero','Marzo'])

lista_gastos = [float(df.loc[df['Enero'] < 0, ['Enero']].sum()),float(df.loc[df['Febrero'] < 0, ['Febrero']].sum()),float(df.loc[df['Marzo'] < 0, ['Marzo']].sum())]
lista_neto = [float(df.Enero.sum()),float(df.Febrero.sum()),float(df.Marzo.sum())]

leyenda = pd.DataFrame({"Posicion": ["1", "2", "3"], "Mes": ["Enero","Febrero","Marzo"]})


# Definimos los test unitarios

def test_gasto_total():
    assert Practica_L2_Jose_Lanzas.gasto_total(df)==-20


def test_ingreso_total():
    assert Practica_L2_Jose_Lanzas.ingreso_total(df)==25


def test_media_gastos():
    assert Practica_L2_Jose_Lanzas.media_gastos(df)==-5


def test_peor_mes():
    assert Practica_L2_Jose_Lanzas.peor_mes(lista_gastos)=='Febrero'


def test_mejor_mes():
    assert Practica_L2_Jose_Lanzas.mejor_mes(lista_neto)=='Marzo'
