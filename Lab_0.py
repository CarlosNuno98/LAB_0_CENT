# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:22:50 2020

@author: carlo
"""

# -- ------------------------------------------------------------------------------------ -- #
# -- Proyecto: Describir brevemente el proyecto en general                                -- #
# -- Codigo: RepasoPython.py - describir brevemente el codigo                             -- #
# -- Repositorio: https://github.com/CarlosNuno98/LAB_O_CENT                              -- #
# -- Autor: Carlos Elias Nuño Tiscareño                                                   -- #
# -- ------------------------------------------------------------------------------------ -- #

# -- ------------------------------------------------------------- Importar con funciones -- #

import funciones as fn                              # Para procesamiento de datos
import visualizaciones as vs                        # Para visualizacion de datos
import pandas as pd                                 # Procesamiento de datos
from datos import OA_Ak                             # Importar token para API de OANDA

# -- --------------------------------------------------------- Descargar precios de OANDA -- #

# token de OANDA
OA_In = "EUR_USD"                  # Instrumento
OA_Gn = "D"                        # Granularidad de velas
fini = pd.to_datetime("2019-07-06 00:00:00").tz_localize('GMT')  # Fecha inicial
ffin = pd.to_datetime("2019-12-06 00:00:00").tz_localize('GMT')  # Fecha final

# Descargar precios masivos
df_pe = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=OA_Gn,
                             p3_inst=OA_In, p4_oatk=OA_Ak, p5_ginc=4900)

# Descargar precios masivos
df_pe = fn.f_precios_masivos(p0_fini=fini, p1_ffin=ffin, p2_gran=OA_Gn,
                             p3_inst=OA_In, p4_oatk=OA_Ak, p5_ginc=4900)

# -- --------------------------------------------------------------- Graficar OHLC plotly -- #

vs_grafica1 = vs.g_velas(p0_de=df_pe.iloc[0:120, :])
vs_grafica1.show()

# -- ------------------------------------------------------------------- Conteno de velas -- #

# multiplicador de precios
pip_mult = 10000

# -- 0A.1: Mes
df_pe['mes'] = [df_pe['TimeStamp'][i].month for i in range(0, len(df_pe['TimeStamp']))]

# -- 0A.1: Hora
df_pe['hora'] = [df_pe['TimeStamp'][i].hour for i in range(0, len(df_pe['TimeStamp']))]

# -- 0A.2: Dia de la semana.
df_pe['dia'] = [df_pe['TimeStamp'][i].weekday() for i in range(0, len(df_pe['TimeStamp']))]

# -- 0B: Boxplot de amplitud de velas (close - open).
df_pe['co'] = (df_pe['Close'] - df_pe['Open'])*pip_mult

# -- ['hl']: Amplitud de extremos (en pips).
df_pe['hl'] = (df_pe['High'] - df_pe['Close'])*pip_mult

 
# -- Sentido de vela, alcista o bajista
df_pe['sentido'] = 


# -- Ventamas moviles de volarilidad
  
  #Volatilidad 5
    
df_pe['Close: 5 Day Mean'] = df_pe['Close'].rolling(window=5).mean()
df_pe[['Close','Close: 5 Day Mean']].plot(figsize=(16,6))
    
    #Volatilidad 25

df_pe['Close: 25 Day Mean'] = df_pe['Close'].rolling(window=25).mean()
df_pe[['Close','Close: 25 Day Mean']].plot(figsize=(16,6))

    #Volatilidad 50

df_pe['Close: 50 Day Mean'] = df_pe['Close'].rolling(window=50).mean()
df_pe[['Close','Close: 50 Day Mean']].plot(figsize=(16,6))


# -- ------------------------------------------------------------ Graficar Boxplot plotly -- #
vs_grafica2 = vs.g_boxplot_varios(p0_data=df_pe[['co']], p1_norm=False)
vs_grafica2.show()










