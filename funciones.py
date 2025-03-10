#1 CARGA DE ARCHIVO
def cargar_dataset(archivo):
    import pandas as pd
    import os

    #si se desea agregar un input se coloca:
    #Archivo = input("Favor ingresa el nombre del archiv")
    extension = os.path.splitext(archivo)[1].lower()   #Al archivo se le saca la extensión
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df =pd.read_excel(archivo)
        return(df)
    else:
            raise ValueError(f"Este formato no está soportado para está función: {extension}")
    

    #######################33
#función 2
def valores_nulos_susti(df):
    import pandas as pd

    #Separar las variables cualitativas de cuantitativas 
    cuantitativas = df.select_dtypes(include=['float64','float','int','int64'])
    cualitativas = df.select_dtypes(include=['object', 'datetime','category'])

    #Seleccionar las pares e impares 
    impares = cuantitativas.iloc[:, ::2]   
    pares = cuantitativas.iloc[:, 1::2]
    
    # sustituir los pares  con .mean 
    pares = pares.fillna(round(pares.mean(),1))

    # Los valores impares que son cuantitativas rellenarlo con 99
    impares = impares.fillna(99)

    #Relleno las cualitativas con strings
    cualitativas = cualitativas.fillna('Este_es_un_valor_nulo')
         
     # Unimos los dataframe spara que se vuelva limpio
    Datos_sin_nulos = pd.concat([pares,impares, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

###############################
#Función 3 

def cuenta_valores_nulos(dataframe):
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()
    
    return("Valores nulos por columna", valores_nulos_cols,
            "Valores nulos por dataframe", valores_nulos_df)

########################################################3
#Fucnión 4

def eliminar_y_graficar_outliers(data):
    #Valores atipicos
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    data.plot(kind='box', vert =False)
    plt.title("Antes de eliminar los valores")
    plt.show()

    cuantitativas = data.select_dtypes(include=['float64', 'int64','float','int'])
    cualitativas = data.select_dtypes(include=['object', 'datetime','category'])

    # Calcular cuartiles e IQR
    y= cuantitativas

    percentiles25 = y.quantile(0.25) #Q1
    percentile75 = y.quantile(0.75) #Q3
    iqr = percentile75 - percentiles25

    Limite_superior_iqr = percentile75 + 1.5*iqr
    Limite_inferior_iqr = percentile75 - 1.5*iqr

    print("Limite superior permitido",Limite_superior_iqr)
    print("Limite inferior permitido",Limite_inferior_iqr)

    data4_iqr = cuantitativas[(y<=Limite_superior_iqr) & (y>=Limite_inferior_iqr)]
    data4_iqr = data4_iqr.fillna(round(data4_iqr.mean(),1))

    dato_limpios = pd.concat([cualitativas, data4_iqr], axis=1)

    return dato_limpios.to_csv("DATOS_LIMPIOS.csv")






